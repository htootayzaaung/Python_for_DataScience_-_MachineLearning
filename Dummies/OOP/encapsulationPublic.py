class Employee:
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def show(self):
        print(f"Name: {self.name}\nSalary: {self.salary}\n")
        
e1 = Employee("Htoo Aung", "$2bn")

e1.show()

print(f"Name: {e1.name}\nSalary: {e1.salary}\n")