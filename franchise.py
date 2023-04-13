from orderfactory import Order_Factory
from logger import logger

class Franchise:
    def __init__(self,number):
        self.location_number =number
    
    def Place_Order(self):
        order = int(input("Welcome to Vince's Pizza! What would you like to order?  Enter '1' for pizza, '2' for pasta, '3' for a salad.:" ))
        orders = Order_Factory.create_order(order) 
        logger.Log_Transaction(orders,self.location_number)   
       #place order () void
    
    
    @staticmethod
    def enjoy():
     print ('Enjoy your meal, thank you for your order')

    
