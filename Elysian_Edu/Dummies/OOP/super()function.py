class Company:
    
    def company_name(self):
        return "Google"
    


class Employee(Company):
    
    def info(self, employee_name):
        c_name = super().company_name()
        print(f"{employee_name} works at {c_name}.")
        
emp1 = Employee()

emp1.info("Htoo Aung")