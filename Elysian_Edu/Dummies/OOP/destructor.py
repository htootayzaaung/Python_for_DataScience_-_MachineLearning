class Student:
    
    def __init__(self, name):
        print("Inside Constructor")
        self.name = name
        print("Object Initialised")
        
    def show(self):
        print(f"Hello, my name is {self.name}")
        
    def _del__(self):
        print("Inside Destructor")
        print("Object Destroyed")
        
s1 = Student("Htoo Aung")

s1.show()

del s1