class Vehicle:
    
    def vehicle_info(self):
        print("Inside Vehicle class")
        


class Car(Vehicle):
    
    def car_info(self):
        print("Inside Car class")
        
        
        
class Truck(Vehicle):
    
    def truck_info(self):
        print("Inside Truck class")
        
        
        
class SportsCar(Car, Vehicle):
    
    def sports_car_info(self):
        print("Inside SportsCar class")
        

s_car1 = SportsCar()

s_car1.vehicle_info()

s_car1.car_info()

s_car1.sports_car_info()


s_car2 = Truck()

s_car2.vehicle_info()

s_car2.truck_info()


s_car3 = Car()

s_car3.car_info()

s_car3.vehicle_info()

