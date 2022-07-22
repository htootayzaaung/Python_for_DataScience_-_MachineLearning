class Person:
    def __init__(self, name, sex, profession):
        #instance variables:
            self.name = name
            self.sex = sex
            self.profession = profession
            
    def showInstanceVariables(self):
        print(f"Name: {self.name}\nSex: {self.sex}\nProfession: {self.profession}")

p1 = Person("Htoo Aung", "Male", "University Student")

p1.showInstanceVariables()

