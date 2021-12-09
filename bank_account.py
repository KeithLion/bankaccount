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
            