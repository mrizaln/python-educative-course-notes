# Challenge 1: Implement a Banking Account

# make an Account class with instance variables (default to None or 0):
    # title 
    # balance

# derive SavingsAccount class from Account with additional instance variable (default to None or 0):
    # interestRate

class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance

class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
        self.interestRate = interestRate
        super().__init__(title, balance)