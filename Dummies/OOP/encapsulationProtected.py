class Company:
    
    def __init__(self):
        self._project = "Natural Language Processing"
        
class Employee(Company):
    
    def __init__(self, name):
        self.name = name
        Company.__init__(self)
        
    def show(self):
        print(f"Employee's name: {self.name}")
        print(f"Current Project: {self._project}")
        
e1 = Employee("Htoo Aung")

e1.show()

print(e1._project)
        
