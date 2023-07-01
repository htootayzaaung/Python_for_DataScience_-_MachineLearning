class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        
    def show(self):
        print(f"Name: {self.name}\nAge: {self.age}\nSalary: {self.salary}")

s1 = Employee("Htoo Aung", 24, "3bn Sterling pounds")

s1.show()