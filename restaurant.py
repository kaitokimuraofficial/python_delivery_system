class Restaurant():
    def __init__(self, restaurant_id, 
                 position_x, position_y, 
                 date_closed_from = -1, date_closed_to = -1):
        self._restaurant_id = restaurant_id
        self._position = [position_x, position_y]
        self._date_closed = [date_closed_from, date_closed_to]
        self._order_list = []
    
    @property
    def restaurant_id(self):
        return self._restaurant_id
    
    @property
    def position(self):
        return self._position
    
    @position.setter
    def position(self, position_x, position_y):
        self._position = [position_x, position_y]
    
    @property
    def date_closed(self):
        return self._date_closed
    
    @date_closed.setter
    def date_closed(self, date_closed_from, date_closed_to):
        self._date_closed = [date_closed_from, date_closed_to]
    
    @property
    def order_list(self):
        return self._order_list
    
    @position.setter
    def position(self, order):
        self._order_list.append(order)

    def calculate_sales(self, date_from, date_to):
        sales = 0
        
        for order in self._order_list:
            if order[0] < date_from or date_to < order[0]:
                continue
            sales += order[1]
        
        return sales

