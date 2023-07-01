class Person:
    
    def person_info(self, name, age):
        print("Inside Person class!")
        print(f"Name: {self.name}\nAge: {self.age}")
        
        
class Company:
    
    def company_info(self, company_name, location):
        print("Inside Company class!")
        print(f"Name: {self.company_name}\nLocation: {self.location}" )
        

class Employee(Person, Company):
    
    def Employee_info(self, salary, skill):
        print("Inside Employee class!")
        print(f"Salary: {self.salary}\nSkill = {self.skill}")
        
p1 = Person()

p1.person_info("Htoo Aung", 20)
        