class Resources:
    
    water = 200000
    milk = 150000
    coffee = 6500
    chocolate = 5000
    revenue = 0



    def show_resources(self):
        print()
        self.show_resources_water()
        self.show_resources_milk()
        self.show_resources_coffee()
        self.show_resources_chocolate()
        self.show_resources_revenue()
        
    def show_resources_water(self):
        if (Resources.water >= 1000 and Resources.water % 1000 == 0):
            print("Water: %dl" % (Resources.water / 1000))
        elif (Resources.water >= 1000 and (Resources.water % 1000) != 0):
            print("Water: %.2fl" % (Resources.water / 1000))
        elif (Resources.water < 1000):
            print(f"Water: {Resources.water}ml")
    
    def show_resources_milk(self):
        if (Resources.milk >= 1000 and Resources.milk % 1000 == 0):
            print("Milk: %dl" % (Resources.milk / 1000))
        elif (Resources.milk >= 1000 and (Resources.milk % 1000) != 0):
            print("Milk: %.2fl" % (Resources.milk / 1000))
        elif (Resources.water < 1000):
            print(f"Milk: {Resources.milk}ml")
        
    def show_resources_coffee(self):
        if (Resources.coffee >= 1000 and Resources.coffee % 1000 == 0):
            print("Coffee: %dkg" % (Resources.coffee / 1000))
        elif (Resources.coffee >= 1000 and (Resources.coffee % 1000) != 0):
            print("Coffee: %.2fkg" % (Resources.coffee / 1000))
        elif (Resources.coffee < 1000):
            print(f"Coffee: {Resources.coffee}g")
    
    def show_resources_chocolate(self):
        if (Resources.chocolate >= 1000 and Resources.chocolate % 1000 == 0):
            print("Chocolate: %dkg" % (Resources.chocolate / 1000))
        elif (Resources.chocolate >= 1000 and (Resources.chocolate % 1000) != 0):
            print("Chocolate: %.2fkg" % (Resources.chocolate / 1000))
        elif (Resources.chocolate < 1000):
            print(f"Chocolate: {Resources.chocolate}g")

    def show_resources_revenue(self):
        print("Revenue: $%.2f" % Resources.revenue)
        


    def check_all_resources(self):
        self.check_resources_water()
        self.check_resources_milk()
        self.check_resources_coffee()
        self.check_resources_chocolate()
        
    def check_resources_water(self):
        if (Resources.water < 50):
            print("Sorry there is not enough water.")
    
    def check_resources_milk(self):
        if ((user_choice == 1 or user_choice == 4) and (Resources.milk < 20)):
            print("Sorry there is not enough milk.")
        elif ((user_choice == 2 or user_choice == 5) and (Resources.milk < 10)):
            print("Sorry there is not enough milk.")
        elif ((user_choice == 3) and (Resources.milk < 30)):
            print("Sorry there is not enough milk.")
    
    def check_resources_coffee(self):
        if ((user_choice == 1 or user_choice == 3) and (Resources.coffee < 10)):
            print("Sorry there is not enough coffee.")
        elif ((user_choice == 2) and (Resources.coffee < 15)):
            print("Sorry there is not enough coffee.")
    
    def check_resources_chocolate(self):
        if ((user_choice == 4) and (Resources.chocolate < 15)):
            print("Sorry there is not enough coffee.")
        if ((user_choice == 5) and (Resources.chocolate < 30)):
            print("Sorry there is not enough coffee.")            



    def update_resources(self):
        Resources.water -= 50
        if(user_choice == 1):
            Resources.milk -= 20
            Resources.coffee -= 10
            Resources.revenue += 2.25
        if(user_choice == 2):
            Resources.milk -= 10
            Resources.coffee -= 15
            Resources.revenue += 2.5
        if(user_choice == 3):
            Resources.milk -= 30
            Resources.coffee -= 10
            Resources.revenue += 3.2
        if(user_choice == 4):
            Resources.milk -= 20
            Resources.chocolate -= 15
            Resources.revenue += 2.35
        if(user_choice == 5):
            Resources.milk -= 10
            Resources.chocolate -= 30   
            Resources.revenue += 3.4
            


    def machine_state_toggle(self):
        state = input ("type ENTER to continue: ")
        if (state == "OFF"):
            exit()
    
    def check_payment(self):
        self.user_payment = str(input("Your bill-code: "))
        self.bill_code_amount = 0
        self.bill_variance = 0
        self.user_payment_splitted = self.user_payment.split(",")
        
        for i in range(len(self.user_payment_splitted)):
            if(self.user_payment_splitted[i][1] == "$"):
                self.bill_code_amount += (int(self.user_payment_splitted[i][0]) * 1)
            if(self.user_payment_splitted[i][1] == "q"):
                self.bill_code_amount += (int(self.user_payment_splitted[i][0]) * 0.25)
            if(self.user_payment_splitted[i][1] == "d"):
                self.bill_code_amount += (int(self.user_payment_splitted[i][0]) * 0.10)
            if(self.user_payment_splitted[i][1] == "n"):
                self.bill_code_amount += (int(self.user_payment_splitted[i][0]) * 0.05)
            if(self.user_payment_splitted[i][1] == "p"):
                self.bill_code_amount += (int(self.user_payment_splitted[i][0]) * 0.001)               
            
        
        if (user_choice == 1):
            self.item_price = 2.25
            self.bill_variance = abs(self.item_price - self.bill_code_amount)
        elif (user_choice == 2):
            self.item_price = 2.4
            self.bill_variance = abs(self.item_price - self.bill_code_amount)
        elif (user_choice == 3):
            self.item_price = 3.2
            self.bill_variance = abs(self.item_price - self.bill_code_amount)
        elif (user_choice == 4):
            self.item_price = 2.35
            self.bill_variance = abs(self.item_price - self.bill_code_amount)            
        elif (user_choice == 5):
            self.item_price = 3.4
            self.bill_variance = abs(self.item_price - self.bill_code_amount)
            
        
        if (self.item_price > self.bill_code_amount):
            print("You need to pay additional $%.2f." % self.bill_variance)
            print("Money refunded. Please try again!")
        elif (self.item_price < self.bill_code_amount):
            print("You have paid $%.2f extra." % self.bill_variance)
            print("Money refunded. Please try again!")
    
    def make_payment(self):
        print("\nInsert banknotes and coins and Enter the corresponding bill-code in the format: \n2$,2q,2d,2n,2p where dollar = $, quarters = q, dimes = d, nikels = n, pennies = p\n")
        self.check_payment()
            
        while(self.item_price - self.bill_code_amount != 0):
            self.check_payment()
            
        if (self.item_price - self.bill_code_amount == 0):
            print("\n*******************************************\nPayment Successfull! Transaction Completed!\n*******************************************")
            


state = "ON"

while (state == "ON" or state == "ENTER"):
    
    s1 = Resources()

    s1.show_resources()

    user_choice = int(input("What would you like?\n\n1.Expresso\n2.Latte\n3.Cappuccino\n4.Chocolate Milkshake\n5.Chocolate Smoothies\n\nEnter options 1-5: "))
    
    s1.make_payment()
    
    s1.check_all_resources()
    
    if (user_choice <= 0 or user_choice > 5):
        
        print("\n*****************\nInvalid Option!\nPlease try again!\n*****************")
        
        user_choice = int(input("Enter options 1-5: "))
        
        s1.make_payment()
        
        s1.check_all_resources()
                                         
    s1.update_resources()
    
    s1.machine_state_toggle()
    

    

