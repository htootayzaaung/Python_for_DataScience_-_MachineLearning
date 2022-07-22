class Vehicle:
    
    def info(self):
        print("This is vehicle!")
        
        
        
class Car(Vehicle):
    
    def car_info(self, name):
        print(f"Car Model: {name}")
        
        
class Truck(Vehicle):
    
    def truck_info(self, name):
        print(f"Truck Model: {name}")
        
obj1 = Car()
obj1.info()
obj1.car_info("BMW")

obj2 = Truck()
obj2.info()
obj2.truck_info("Ford")