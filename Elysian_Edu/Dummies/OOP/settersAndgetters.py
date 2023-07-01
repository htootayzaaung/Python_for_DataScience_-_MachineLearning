#Getter methods are used to access data and setter methods are used to modify the data members

class Student:
    
    def __init__(self, name, age):
        self.name = name;
        self.__age = age;
        
    def get_age(self):
        return self.__age
    
    def set_age(self, age):
        self.__age = age
        
s1 = Student("Htoo Aung", 20)

print(f"Name: {s1.name}\nAge: {s1._Student__age}\n")

print(f"Name: {s1.name}\nAge: {s1.get_age()}\n")

s1.set_age(21)

print(f"Name: {s1.name}\nAge: {s1._Student__age}\n")

print(f"Name: {s1.name}\nAge: {s1.get_age()}\n")