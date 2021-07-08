class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
    	self.account_balance += amount	# the specific user's account increases by the amount of the value received
    def make_withdrawl(self, amount): # takes an argument that is the amount of the withdrawl
        self.account_balance -= amount # the specific user's account decreases by the amount of the value withdrawn
    def display_user_balance(self): # This was busted until I remembered my () FACEPALM
        print(self.name)
        print(self.account_balance)

guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")

travis = User("Travis Douglass", "TDugzzz@HaloReach.com")
maddox = User("Maddox Womble", "MadFox420@WSMFP.com")