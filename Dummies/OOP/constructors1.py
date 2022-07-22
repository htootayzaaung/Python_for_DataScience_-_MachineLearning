class Student:
    def __init__(self, name):
        print("Inside a constructor...")
        self.name = name
        print("All variables iniitalised. End of constructor...")
        
    def show(self):
        print(f"My name is {self.name}.")
        
s1 = Student("Htoo Aung")
s1.show()