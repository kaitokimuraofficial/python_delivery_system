import unittest

import util

class UtilTest(unittest.TestCase):
    def test_split_date(self):
        year, month, day = util.split_date("2020-03-04")
        self.assertEqual(year, 2020)
        self.assertEqual(month, 3)
        self.assertEqual(day, 4)
    
    def test_split_time(self):
        hour, minute = util.split_time("10-30")
        self.assertEqual(hour, 10)
        self.assertEqual(minute, 30)
    
    def test_split_order_info(self):
        res_id, price, destination_x, destination_y = util.split_order_info(["iVehD", "5000", "140", "0"])
        self.assertEqual(res_id, "iVehD")
        self.assertEqual(price, 5000)
        self.assertEqual(destination_x, 140)
        self.assertEqual(destination_y, 0)

    def test_set_available_order_info(self):
        deliveryman_id, position_x, position_y = util.split_set_available_info(["Bob", "50", "0"])
        self.assertEqual(deliveryman_id, "Bob")
        self.assertEqual(position_x, 50)
        self.assertEqual(position_y, 0)



if __name__ == "__main__":
    unittest.main()