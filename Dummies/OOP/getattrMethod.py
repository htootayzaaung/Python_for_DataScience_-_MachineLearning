class Student:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
s1 = Student("Htoo Aung", 20)

name_temp = getattr(s1, "name")
age_temp = getattr(s1, "age")

print(f"Name: {name_temp}\nAge: {age_temp}")