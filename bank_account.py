class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdrawl(self, amount):
        if self.balance + amount > 0:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging $32")
            self.balance -= 32

    def display_account_info(self):
        print(self.balance + " in your account")

    def yield_interest(self):
        self.balance = self.balance * 1.02

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.balance = 0

travis = User("Travis Douglass", "TDugzzz@HaloReach.com")
maddox = User("Maddox Womble", "MadFox420@WSMFP.com")

