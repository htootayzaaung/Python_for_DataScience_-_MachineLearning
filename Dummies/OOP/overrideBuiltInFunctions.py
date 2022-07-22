class Shopping:
    
    def __init__(self, basket, buyer):
        self.basket = basket
        self.buyer = buyer
        
    def __len__(self):
        print("Redifining length")
        count = len(self.basket)
        return count * 2
    
trolley1 = Shopping(["Eggs", "Sausages"], "Matthew")

print(len(trolley1))