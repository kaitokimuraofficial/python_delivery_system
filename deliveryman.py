DELIVERING  =  0
AVAILAVLE   =  1
UNAVAILABLE = -1

class Deliveryman():
    def __init__(self, deliveryman_id, 
                 position_x=None, position_y=None, 
                 condition=1, max_delivery_time=1000000000000,
                 date_available_from = -1):
        self._deliveryman_id = deliveryman_id
        self._position = [position_x, position_y]
        self._condition = condition
        self._max_delivery_time = max_delivery_time
        self._date_available_from = date_available_from
    
    @property
    def deliveryman_id(self):
        return self._deliveryman_id

    @property
    def position(self):
        return self._position
    
    @position.setter
    def position(self, position):
        self._position = position

    @property
    def condition(self):
        return self._condition
    
    @condition.setter
    def condition(self, condition):
        self._condition = condition
    
    @property
    def max_delivery_time(self):
        return self._max_delivery_time
    
    @max_delivery_time.setter
    def max_delivery_time(self, max_delivery_time):
        self._max_delivery_time = max_delivery_time
    
    @property
    def date_available_from(self):
        return self._date_available_from
    
    @date_available_from.setter
    def date_available_from(self, date_available_from):
        self._date_available_from = date_available_from



