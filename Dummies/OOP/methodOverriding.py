class Vehicle:
    
    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price
        
    def show(self):
        print(f"Name = {self.name}\nColor = {self.color}\nPrice = {self.price}\n")
     
    def max_speed(self):
        print("Vehicle max speed is 150")
        
    def change_gear(self):
        print("Vehicle change 6 gear")
        

class Car(Vehicle):
    
    def max_speed(self):
        print("Car max-speed is 240")
        
    def change_gear(self):
        print("Car change 7 gear")
        

c1 = Car("Car x1", "Violet", 20000)

c1.show()

c1.max_speed()

c1.change_gear()

t1 = Vehicle("Truck pl620", "Green", 34500)

t1.max_speed()

t1.change_gear()
        