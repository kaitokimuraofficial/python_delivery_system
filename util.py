def split_date(date):
    year = int(date[0:4])
    month = int(date[5:7])
    day = int(date[9:11])

    return [year, month, day]

def split_time(time):
    hour = int(time[0:2])
    minute = int(time[3:5])
    if hour == 24 and minute == 0:
        return [-1, -1]

    return [hour, minute]

def get_datetime(date, time):
    import datetime
    year, month, day = split_date(date)
    hour, minute = split_time(time)

    if hour < 0:
        cur = datetime.datetime(year, month, day, 0, 0)
        return cur + datetime.timedelta(days=1)
    
    return datetime.datetime(year, month, day, hour, minute)


def split_order_info(other_info):
    res_id = other_info[0]
    price = int(other_info[1])
    destination_x = int(other_info[2])
    destination_y = int(other_info[3])

    return [res_id, price, destination_x, destination_y]

def split_set_available_info(other_info):
    deliveryman_id = other_info[0]
    position_x = int(other_info[1])
    position_y = int(other_info[2])

    return [deliveryman_id, position_x, position_y]

def calculate_manhattan_dis(from_x, from_y, to_x, to_y):
    dis_x = abs(from_x - to_x)
    dis_y = abs(from_y - to_y)

    return dis_x + dis_y


def calculate_expected_dis(man, res, destination):
    dis_outward = calculate_manhattan_dis(man.position[0], man.position[1], res.position[0], res.position[1])
    dis_return = calculate_manhattan_dis(res.position[0], res.position[1], destination[0], destination[1])

    return dis_outward + dis_return


def calculate_free_time(man, current_datetime):
    import datetime
    return current_datetime - man.date_available_from

def calculate_delivery_charge(distance):
    if distance < 100:
        return 300
    elif distance < 1000:
        return 600
    elif distance < 10000:
        return 900
    else:
        return 1200