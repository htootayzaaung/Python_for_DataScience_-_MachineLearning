class Vehicle:
    
    def Vehicle_info(self):
        print("Inside Vehicle Class")
        
class Car(Vehicle):
    
    def Car_info(self):
        print("Inside Car Class")
        
c1 = Car()

c1.Vehicle_info()

c1.Car_info()
