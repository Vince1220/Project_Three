from order import Order
class Order_Factory:
    choice = int(input("Welcome to Vince's Pizza! Choose from the menue and enter 1-3:" ))
    if choice == 1:
        print ()
        print (f'You chose {Order.Pizza.pizza_dish} and your price is {Order.Pizza.pizza_price}')
    elif choice == 2:
        print ()
        print(f'You chose{Order.Pasta.pasta_dish} and your price is {Order.Pasta.pasta_price}')
    elif choice == 3:
        print ()
        print (f'You chose {Order.Salad.salad_dish} and your price is {Order.Salad.salad_price}')

    @staticmethod
    def enjoy():
        print ('Enjoy your meal, thank you for your order')
    #create order (string) : Order static
    pass
