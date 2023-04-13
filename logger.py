from order import Order
from orderfactory import Order_Factory

class Logger:

    def __init__(self):
        self.transaction_count = 1
        self.daily_sales = 0
        #daily sales int
    
    def Log_Transaction(self,order,location_number):
        self.daily_sales += order.price
        file = open('log.txt','a')
        if order is  not None:
            self.transaction_count =1
            self.transaction_count += 1
        file.write (f'{self.transaction_count}Dish ordered: {order.dish_name},from location {location_number},Price: {order.price},Total {self.daily_sales}\n')
        file.close()    
        
        
logger= Logger()
        #log transaction (order,int): void
