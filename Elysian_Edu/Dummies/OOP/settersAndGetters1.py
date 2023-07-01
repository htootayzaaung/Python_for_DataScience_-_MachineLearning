class Student:

    def __init__(self, name, roll_no, age):
        self.name = name
        self.__roll_no = roll_no
        self.__age = age
        
    def show(self):
        print(f"Name: {self.name}\nRoll no: {self._Student__roll_no}\nAge: {self._Student__age}\n")        

    def get_roll_no(self):
        return self.__roll_no
    
    def set_roll_no(self, number):
        if (number > 50):
            print("Invalid roll no. Please set the correct roll no.")
        else:
            self.__roll_no = number
            
s1 = Student("Htoo Aung", 13, 20)

s1.show()

s1.set_roll_no(25)

s1.show()

s1.set_roll_no(51)

        
        