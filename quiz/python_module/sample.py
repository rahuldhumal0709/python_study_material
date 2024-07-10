
# if (9<0 and 0< -9):
#     print("hello")
# elif (9>0 or False):
#     print("good")
# else:
#     print("bad")
# print(not(3>4))
# print(not(1&1))
# a=["abc","bcd",'cde']
# b-c=["tom"]
# li = [1,2,3,2]
# li.remove(2)
# print(li)
#print(ord('foo'))
# s='foo'
# t='bar'
# print("barf" in 2 * (s+t))
# print(2*(s+t))

# print('p'+'q',end='')
# if '12'.isdigit():
#     print('12')
# else:
#     print('r'+'s')
#print('hello'=="hello")
# i=1
# while True:
#     if i%3==0:
#         break
#     print(i)
#    i=i+1
# s1='rahul'
# s2='dhumal'
# s3=s1+s2
# print(s3)
#print(chr(ord('b')+1))

# x='abcd'
# for i in range(len(x)):
#     x='a'
#     print(x)

# for i in range(0):
#     print(i)

#print('ab,cd,ef,cd,gh.cd'.split(','))
# str1="rahul"
# for i in range(len(str1)):
#     print(str1[i])

# lst=["Rahul","Virat","Rohit","Surya"]
# for i in lst:
#     print(i)
#     ends_with = lst.endswith("t")
# print(ends_with)
# from re import L


# lst=[5,7,4,6,8,2,3,5,2]
# lst1=set(lst)
# lst=list(lst1)
# print(lst)
# for i in range(0,len(lst)):
#     for j in range(i+1,len(lst)):
#         if lst[i]==lst[j]:
#             lst.remove(lst[i])
# print(lst1)

# s = 'linkedin'
# print(s.find('m'))
# if "n" in s:
#     print("true")
# else:
#     print("false")

# print(list(range(-3,10,3)))
# class Student:
#     __name = "Rahul"
#     roll_no = 1
#     def setName(self,name):
#         self.__name = name
#     def getName(self):
#         return self.__name
#     def setroll_no(self,roll_no):
#         self.roll_no = roll_no
#     def getName(self):
#         return self.roll_no
# name = input("Enter name: ")
# roll_no = input("Enter roll no: ")
# obj=Student()
# print("Before setter : ",obj.__dict__)
# obj.setName(name)
# obj.setroll_no(roll_no)
# print("After setter : ",obj.__dict__)
# import datetime
# def gettime():
#     return datetime.datetime.now()
# class ATM:
#     def __init__(self):
#         self.pin = '7999'
#         self.balance = 10000
#         # ask for pin
#     def check_pin(self):
#         self.entered_pin=input('Enter your pin : ')
#         # check if pin is correct or not
#         if self.pin==self.entered_pin and len(self.pin)==4 and self.pin.startswith('0')==False:
#             self.choice=int(input("Enter 1 for deposit,2 for withdrawal and 3 for mini statement : "))
#             if self.choice==1:
#                 obj.deposit(self.choice)
#             elif self.choice==2:
#                 obj.withdrawal(self.choice)
#             elif self.choice==3:
#                 obj.getstatement(self.choice)
#             else:
#                 print("Please enter only given options 1,2 or 3.")
#         else:
#             try:
#                 raise #InvalidPinError()
#             except Exception as ex:
#                 print(ex)
#     # deposit amount
#     def deposit(self,choice): 
#         self.deposit_amount = int(input("Enter amount for deposit : "))
#         # check if entered deposit amount is valid or not
#         if self.deposit_amount <=25000 and str(self.deposit_amount).endswith("00"):
#             with open("bank_statement.txt","a") as file:
#                 self.balance = self.balance + self.deposit_amount
#                 file.write(str([str(gettime())])+f" Deposit amount : {self.deposit_amount} , Total Balance : {self.balance} \n------------------------------------------------------------------------------\n")
#                 print("Amount deposit successfully")              
#         else:
#             try:
#                 raise #InvalidAmountError()
#             except Exception as ex:
#                 print(ex)
#     # withdrawal amount
#     def withdrawal(self,choice):
#         self.withdrawal_amount = int(input("Enter amount for withdrawal : "))
#         # check if entered withdrawal amount is valid or not
#         if self.withdrawal_amount <=25000 and self.withdrawal_amount <= self.balance and str(self.withdrawal_amount).endswith("00"):
#             with open("bank_statement.txt","a") as file:
#                 self.balance = self.balance - self.withdrawal_amount
#                 file.write(str([str(gettime())])+f" Withdraw amount : {self.withdrawal_amount} , Total Balance : {self.balance} \n------------------------------------------------------------------------------\n")
#                 print("Amount withdrawal successfully")              
#         else:
#             try:
#                 raise #InvalidAmountError()
#             except Exception as ex:
#                 print(ex)
#     # mini statement
#     def getstatement(self,choice):
#         with open("bank_statement.txt") as file:
#             data=file.read()
#             print(data)
# obj=ATM()
# obj.check_pin()
class Admn:
    Food_Items_list=[]
    def __init__(self,FoodID,Food_Name,Quantity,Price,Discount,Stock):
        self.__FoodID = FoodID
        self.__Food_Name = Food_Name
        self.__Quantity = Quantity
        self.__Price = Price
        self.__Discount = Discount
        self.__Stock = Stock

    def __str__(self):
        return f"Food ID : {self.__FoodID} \nFood Name : {self.__Food_Name} \nQuantity : {self.__Quantity} \nPrice : {self.__Price} \nDiscount : {self.__Discount} \nStock Price : {self.__Stock}"

    def set_FoodID(self,FoodID):
        self.__FoodID = FoodID

    def get_FoodID(self):
        return self.__FoodID

    def set_Food_Name(self,Food_Name):
        self.__Food_Name = Food_Name

    def get_Food_Name(self):
        return self.__Food_Name

    def set_Quantity(self,Quantity):
        self.__Quantity = Quantity

    def get_Quantity(self):
        return self.__Quantity

    def set_Price(self,Price):
        self.__Price = Price

    def get_Price(self):
        return self.__Price

    def set_Discount(self,Discount):
        self.__Discount = Discount

    def get_Discount(self):
        return self.__Discount

    def set_Stock(self,Stock):
        self.__Stock = Stock

    def get_Stock(self):
        return self.__Stock

    def search_food_by_ID(self,FoodID):
        for foods in self.Food_Items_list:
            if self.get_FoodID() == FoodID:
                return foods
        print("No such Food ID Found!!")

    def Place_new_order(self):
        print("Select your food\n")
        FoodID=int(input("Enter Food ID : "))
        self.Order = self.search_food_by_ID(FoodID)
        if self.Order:
            print(self.Order)
        print("place an order")
        confirmation = input("Please confirm Yes or No : ")
        if confirmation=="Yes":
            print("Order Placed Successfully\n")
        if confirmation=="No":
            print("Order Cancelled")