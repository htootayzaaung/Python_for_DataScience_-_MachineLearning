class Employee:
    
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary
        
    def show(self):
        print(f"Name: {self.name}\nSalary: {self.__salary}\n")

e1 = Employee("Htoo Aung", "$2bn")

e1.show() #This will print out accordance to show() method

#However, the following line will not be printed because salary is a private member thus, it cannot be 
#accessed outside the class

print(f"Name: {e1.name}\nSalary: {e1._Employee__salary}\n")

