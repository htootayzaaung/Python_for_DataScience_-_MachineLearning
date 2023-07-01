class Person:
    def __init__(self, name, sex, profession):
        self.name = name
        self.sex = sex
        self.profession = profession
        
    def show(self):
        print(f"Name: {self.name}\nSex: {self.sex}\nProfession: {self.profession}")
        
Jessica = Person("Jessica", "Female", "Software Engineer")

Jessica.show()