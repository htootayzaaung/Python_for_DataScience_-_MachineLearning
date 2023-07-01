class Student:
    
    def __init__(self, name, age = 12, class_room_capacity = 7):
        self.name = name
        self.age = age
        self.class_room_capacity = class_room_capacity
        
    def show(self):
        print(f"Name: {self.name}\nAge = {self.age}\nClass size: {self.class_room_capacity}")
        
s1 = Student("Htoo Aung")

s1.show()