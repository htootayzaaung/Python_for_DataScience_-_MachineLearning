class Student:
    def __init__(self, roll_no):
        self.roll_no = roll_no
        
        def instanceMethod(self):
            print("Instance method!")
            
        @classmethod
        def classMethod(variable1, variable2):
            print("Class mehtod!")
            
        @staticmethod
        def staticMethod(variable1):
            print("Static method!")
            
jessica = Student("Roll_No: 12324234")

print(jessica.instanceMethod())

Student.classMethod(1, 2)

jessica.staticMethod("11")