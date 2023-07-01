class Student:
    
    def __init__ (self, name):
        print("One argument constructor")
        self.name = name
        
    def __init__ (self, name, age):
        print("Two arguments constructor")
        self.name = name
        self.age = age
    
    def showArgument1(self, name):
        print(f"Name: {self.name}")
        
    def showArguments2(self, name, age):
        print("fName: {self.name}\nAge: {self.age}")
        
emma = Student("Emma")
kelly = Student("Kelly", 21)



"""
Python does not support overloading!
Python does not support overloading!
Python does not support overloading!
Python does not support overloading!
Python does not support overloading!
Python does not support overloading!
Python does not support overloading!
Python does not support overloading!
Python does not support overloading!
Python does not support overloading!
"""