from franchise import Franchise
class Simulation:
    def Run_Simulation(self):
     franchise_one = Franchise(1)
     franchise_two = Franchise(2)
     franchise_three = Franchise(3)

     franchise_one.Place_Order() 
     franchise_two.Place_Order()
     franchise_three.Place_Order()  
     franchise_three.Place_Order()
     franchise_two.Place_Order() 
     franchise_one.Place_Order() 

