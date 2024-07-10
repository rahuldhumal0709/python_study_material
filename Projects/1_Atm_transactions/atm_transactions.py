from custom_exception import InvalidPinError,InvalidAmountError,MaximumAmountError,LessAmountError
import datetime
def gettime():
    return datetime.datetime.now()
class ATM:
    def __init__(self):
        self.pin = '1999'
        self.balance = 20000
    def check_pin(self):
        self.entered_pin=input('Enter your pin : ')  # ask for pin
        # check if entered pin is correct or not
        if self.pin==self.entered_pin and len(self.pin)==4 and self.pin.startswith('0')==False:
            while True:
                self.choice=int(input("Enter \n1.deposit \n2.withdrawal \n3.mini statement \n0.Exit\n"))
                if self.choice==1:
                    obj.deposit()
                elif self.choice==2:
                    obj.withdrawal()
                elif self.choice==3:
                    obj.getstatement()
                elif self.choice==0:
                    print("***** Thank You *****")
                    exit()
                else:
                    print("You entered wrong choice!!")
                    break
        else:
            try:
                raise InvalidPinError()
            except Exception as ex:
                print(ex)

    # deposit amount
    def deposit(self): 
        self.deposit_amount = int(input("Enter amount for deposit : "))
        # check if entered deposit amount is valid or not
        if self.deposit_amount <=25000 and (self.deposit_amount % 100)==0:
            with open("Atm_statement.txt","a") as file:
                self.balance = self.balance + self.deposit_amount
                file.write(str([str(gettime())])+f" Deposit  amount : {self.deposit_amount} , Total Balance : {self.balance} \n------------------------------------------------------------------------------\n")
                print("Amount deposit successfully.")              
        else:
            try:
                if self.deposit_amount>25000:
                    raise MaximumAmountError()
                else:
                    raise InvalidAmountError
            except Exception as ex:
                print(ex)

    # withdrawal amount
    def withdrawal(self):
        self.withdrawal_amount = int(input("Enter amount for withdrawal : "))
        # check if entered withdrawal amount is valid or not
        if self.withdrawal_amount <=25000 and self.withdrawal_amount <= self.balance and (self.withdrawal_amount % 100)==0:
            with open("Atm_statement.txt","a") as file:
                self.balance = self.balance - self.withdrawal_amount
                file.write(str([str(gettime())])+f" Withdraw amount : {self.withdrawal_amount} , Total Balance : {self.balance} \n------------------------------------------------------------------------------\n")
                print("Amount withdrawal successfully.")              
        else:
            try:
                if self.withdrawal_amount>25000:
                    raise MaximumAmountError()

                elif self.withdrawal_amount>self.balance:
                    raise LessAmountError()
                    
                else:
                    raise InvalidAmountError
            except Exception as ex:
                print(ex)

    # mini statement
    def getstatement(self):
        with open("Atm_statement.txt") as file:
            data=file.read()
            print("\nMini statement :\n")
            print(data)
obj=ATM()
obj.check_pin()