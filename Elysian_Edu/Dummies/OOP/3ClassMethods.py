class Student:
    school_name = "University of Leeds"
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def show(self):
        print(f"Student: {self.name}\nAge: {self.age}")
            
    @classmethod
    def changeSchool(class_name, new_name):
        print(f"Previous school name: {class_name.school_name}")
        class_name.school_name = new_name
        print(f"Previous school name: {class_name.school_name}")
            
s1 = Student("Htoo Aung", 21)
s1.show()

s1.changeSchool("Imperial College London")
Student.changeSchool("University College London")