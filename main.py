import io
import sys

_INPUT = """\
2
Lotte 100 200
Macdn 1000 -200
2020-03-04 09:30 set_available Bob 50 -10
2020-03-04 09:33 set_available Jane 830 100
2020-03-04 10:02 order Lotte 2000 200 100
2020-03-04 10:10 set_available Kate 2030 100
2020-03-04 10:11 set_max_delivery_time Kate 10
2020-03-04 10:22 order Macdn 2000 200 100
2020-03-04 10:30 set_unavailable Kate
2020-03-04 10:32 order Lotte 2000 200 100
2020-03-04 10:40 set_available Kate 900 0
2020-03-04 10:52 order Lotte 2000 200 100
2020-03-04 23:59 calculate_sales Lotte 2020-03-04 00:00 2020-03-04 24:00
2020-03-05 00:00 calculate_wages Kate 2020-03-04 09:00 2020-03-04 12:00
"""

sys.stdin = io.StringIO(_INPUT)


import sys
import util
from restaurant import Restaurant
from deliveryman import Deliveryman

import datetime

AVAILAVLE   =  1
UNAVAILABLE = -1
ERROR_NO_DELIVERY_PERSON = "ERROR NO DELIVERY PERSON"
ERROR_CANNOT_SET_UNAVAILAVLE = "ERROR CANNOT SET UNAVAILAVLE"

# レストランのIDとレストランの紐付け
restaurant_table = {}

# 配達員のIDと配達員の紐付け
deliveryman_table = {}


def main(lines):
    ln = len(lines)
    restaurant_count = int(lines[0])
    # 各レストランの宣言とrestaurant_tableへの追加
    for i in range(1, restaurant_count+1):
        res_info = lines[i]
        res_id, res_x, res_y = map(str, res_info.split())
        restaurant_table[res_id] = Restaurant(res_id, int(res_x), int(res_y))
    
    # クエリの処理
    for i in range(restaurant_count+1, ln):
        query = lines[i]
        date, time, order, *other_info = list(map(str, query.split()))
        # 現在時刻を取得
        current_datetime = util.get_datetime(date, time)

        if order == "order":
            res_id, price, *destination = util.split_order_info(other_info)

            # レストランIDから該当のレストランを取得
            res = restaurant_table[res_id]

            man_id, distance = find_who_is_best_deliveryman(res, destination, current_datetime)
            minute_needed = distance * 60 / 100000

            if man_id == None:
                print(date, time, ERROR_NO_DELIVERY_PERSON)

            else:
                money = util.calculate_delivery_charge(distance)
                res.order_list.append([current_datetime, price-money])
                deliveryman_table[man_id].delivery_list.append([current_datetime, money, minute_needed])
                print(date, time, man_id, money)


        if order == "set_available":
            deliveryman_id, position_x, position_y = util.split_set_available_info(other_info)
            
            # もし与えられた配達員IDがtableになければ新しく追加
            if deliveryman_id not in deliveryman_table.keys():
                temp = Deliveryman(deliveryman_id, position_x, position_y)
                temp.date_available_from = current_datetime
                deliveryman_table[deliveryman_id] = temp
            
            man = deliveryman_table[deliveryman_id]

            if man.condition != AVAILAVLE:
                man.date_available_from = current_datetime

            man.condition = AVAILAVLE
            man.position = [position_x, position_y]
        

        if order == "set_unavailable":
            man_id = other_info[0]
            man = deliveryman_table[deliveryman_id]

            if man.condition != AVAILAVLE:
                print(date, time, ERROR_CANNOT_SET_UNAVAILAVLE)
            
            else:
                man.condition = UNAVAILABLE
        

        if order == "set_max_delivery_time":
            man_id, max_delivery_time = other_info[0], int(other_info[1])

            # もし与えられた配達員IDがtableになければ新しく追加
            if man_id not in deliveryman_table.keys():
                temp = Deliveryman(man_id)
                temp.date_available_from = current_datetime
                deliveryman_table[man_id] = temp
            
            man = deliveryman_table[man_id]

            man.max_delivery_time = max_delivery_time
        

        if order == "calculate_sales":
            res_id, date_from, time_from, date_to, time_to = other_info
            # 集計する時刻のスタート
            frm = util.get_datetime(date_from, time_from)
            # 集計する時刻の終わり
            to = util.get_datetime(date_to, time_to)

            res = restaurant_table[res_id]

            sales = res.calculate_sales(frm, to)

            print(date, time, "SALES", sales)

        if order == "calculate_wages":
            man_id, date_from, time_from, date_to, time_to = other_info
            # 集計する時刻のスタート
            frm = util.get_datetime(date_from, time_from)
            # 集計する時刻の終わり
            to = util.get_datetime(date_to, time_to)

            man = deliveryman_table[man_id]

            wages = man.calculate_wages(frm, to)

            print(date, time, "WAGeS", wages)



      



def find_who_is_best_deliveryman(res, destination, current_datetime):
    total_dis = 1000000000000000
    man_id = None
    free_time = None

    for key in deliveryman_table.keys():
        temp_man = deliveryman_table[key]

        if temp_man.condition != AVAILAVLE:
            continue
        
        if len(temp_man.delivery_list) > 0:
            last_order = temp_man.delivery_list[-1]
            available_from = last_order[0] + datetime.timedelta(minutes=last_order[2])

            if available_from > current_datetime:
                continue
        
        free_for = util.calculate_free_time(temp_man, current_datetime)
        expected_dis = util.calculate_expected_dis(temp_man, res, destination)

        if expected_dis > temp_man.max_delivery_time * 10000 / 60:
            continue

        if total_dis > expected_dis:
            man_id = key
            total_dis = expected_dis
            free_time = free_for

        elif total_dis == expected_dis:
            if free_time > free_for:
                man_id = key
    
    return man_id, total_dis



if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)

