from order import Order
class Pizza(Order):
    def __init__(self):
        super().__init__('Pizza',10)
        print ('You ordered pizza.')