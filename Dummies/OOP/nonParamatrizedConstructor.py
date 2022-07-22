class Company:
    def __init__(self):
        self.name = "Default Name"
        self.address = "Default Address"
        
    def show(self):
        print(f"Name: {self.name}\nAddress: {self.address}")
        
c1 = Company()
c1.show()

             