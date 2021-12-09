class BankAccount:

    def __init__(self,int_rate,balance):
        self.intrest = int_rate
        self.account = balance

    def deposit(self,amount):
        self.account += amount
        return self

    def withdraw(self,amount):
        if(self.account - amount) > 0:
            self.account -= amount
        else:
            print('insufficient funds: charging $5 fee')
            self.account - 5

    def display_account(self):
        print(f'Balance:{self.account}')

    def yield_intrest(self):
        if(self.account > 0):
            self.account += self.account*0.07


