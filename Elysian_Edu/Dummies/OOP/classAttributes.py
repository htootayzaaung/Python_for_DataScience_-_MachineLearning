class Student:
    school_name = "ABC School"
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def show(self):
        print(f"School: {self.school_name}\nName: {self.name}\nAge: {self.age}\n")
        
    def show1(self):
        print(f"School: {Student.school_name}\nName: {self.name}\nAge: {self.age}\n")
        
        
s1 = Student("Harry", 12)
s2 = Student("Stuart", 16)

s1.show()
s2.show()

s1.show1()
s2.show1()

Student.school_name = "Imperial College London"
s3 = Student("Htoo Aung", 25)

s3.show()
s3.show1()
