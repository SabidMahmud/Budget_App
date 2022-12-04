class Category:
    def __init__(self, category_name):
        self.category_name = category_name
        self.ledger = []
        self.__balance = 0.00
    def deposit(self, amount, details=""):
        self.ledger.append({"amount": amount, "description": details})
        self.__balance += amount
    def withdraw(self, amount = 0, details = ''):
        if self.check_funds(amount):
            self.ledger.append({"amount": amount*-1, "description": details})
            self.__balance -= amount
            return True
        return False
    def transfer(self, amount, where):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {where.category_name}")
            where.deposit(amount, f"Transfer from {self.category_name}")
            return True
        return False
    def get_balance(self):
        return (self.__balance)
    def check_funds(self, amount):
        if self.__balance > amount:
            return True
        return False

    def __str__(self):
        header = self.category_name.center(30, "*") + "\n"
        ledger = ""
        for item in self.ledger:
            # format description and amount
            line_description = "{:<23}".format(item["description"])
            line_amount = "{:>7.2f}".format(item["amount"])
            # Truncate ledger description and amount to 23 and 7 characters respectively
            ledger += "{}{}\n".format(line_description[:23], line_amount[:7])
        total = "Total: {:.2f}".format(self.__balance)
        return header + ledger + total


def create_spend_chart(categories):
    spent_amounts = []
    # Get total spent in each category
    for cat in categories:
        spent = 0
        for item in cat.ledger:
            if item["amount"] < 0:
                spent += abs(item["amount"])
        spent_amounts.append(round(spent, 2))

    # Calculate percentage rounded down to the nearest 10
    total = round(sum(spent_amounts), 2)
    spent_percentage = list(map(lambda amount: int((((amount / total) * 10) // 1) * 10), spent_amounts))

    # Create the bar chart substrings
    header = "Percentage spent by category\n"

    chart = ""
    for value in reversed(range(0, 101, 10)):
        chart += str(value).rjust(3) + '|'
        for percent in spent_percentage:
            if percent >= value:
                chart += " o "
            else:
                chart += "   "
        chart += " \n"

    footer = "    " + "-" * ((3 * len(categories)) + 1) + "\n"
    descriptions = list(map(lambda category: cat.category_name, categories))
    max_length = max(map(lambda description: len(description), descriptions))
    descriptions = list(map(lambda description: description.ljust(max_length), descriptions))
    for x in zip(*descriptions):
        footer += "    " + "".join(map(lambda s: s.center(3), x)) + " \n"

    return (header + chart + footer).rstrip("\n")