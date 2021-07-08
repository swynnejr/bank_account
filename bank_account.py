class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        # self.name = User

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdrawl(self, amount):
        if self.balance < amount:
            print("We took $5 that you don't even have.")
            self.balance -= (amount + 5)
            return self
        else:
            self.balance -= amount
            return self


    def display_account_info(self):
        print(f'Your balance is: {self.balance}')


    def yield_interest(self):
        self.balance += self.int_rate * self.balance
        return self
# class User:
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#         self.balance = 0

account1 = BankAccount(.02, 100)
account2 = BankAccount(.02, 100)
account3 = BankAccount(.02, 100)


account1.deposit(350).deposit(475).deposit(225).withdrawl(14).yield_interest().display_account_info()

account2.withdrawl(400).display_account_info()

account3.deposit(125).deposit(900).withdrawl(19).withdrawl(42).withdrawl(7).withdrawl(19).yield_interest().display_account_info()