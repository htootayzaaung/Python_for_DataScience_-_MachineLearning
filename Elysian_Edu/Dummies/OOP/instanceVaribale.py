class Student:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def show(self):
        print(f"Name: {self.name}\nAge: {self.age}")
        
s1 = Student("Htoo Aung", 20)

s1.show()

