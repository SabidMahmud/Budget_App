class Category:
    def __init__(self, category_name):
        self.cat_name = category_name
    
    def deposit(self, amount, details = None):
        self.deposit_amount = amount
        self.deposit_type = details
    def withdraw(self, amount = 0, details = ''):
        self.withdraw_amount = amount
        self.withdraw_details = details
    
    def transfer(self, amount, transfer_here):
        self.transfer_amount = amount
        transfer_here.deposit_amount += self.transfer_amount
    def get_balance(self):
        return self.deposit_amount - self.withdraw_amount
        







# def create_spend_chart(categories):
#     pass 

food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food)
print(clothing)