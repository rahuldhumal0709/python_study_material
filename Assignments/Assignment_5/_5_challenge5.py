class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance
    
    def withdrawal(self, withdrawal_amount):
        self.withdrawal_amount = withdrawal_amount
        self.balance = self.balance - self.withdrawal_amount
      
    def deposit(self, deposit_amount):
        self.deposit_amount = deposit_amount
        self.balance = self.balance + self.deposit_amount

    def getbalance(self):
        return self.balance

class SavingsAccount(Account):
    def __init__(self,title=None,balance=0,interestRate=0):
        super().__init__(title, balance)
        self.balance = balance
        self.interestRate = interestRate

    def interestAmount(self):
        self.interest_amount = (self.interestRate * self.balance)/100
        return self.interest_amount
obj = SavingsAccount('Ashish',10000,5)
deposit_amount = int(input("Enter deposit amount : "))
obj.deposit(deposit_amount)
print("After deposit:Total Amount is: ",obj.getbalance())
withdrawal_amount = int(input("Enter withdrawal amount : "))
obj.withdrawal(withdrawal_amount)
print("After withdrawal:Total remaining amount is: ",obj.getbalance())
print("Interest Amount : ",obj.interestAmount())