# import package1.module1  #---1st way
# import package1.module1 as md #--->2nd way
# from package1.module1 import one,three,name #--->3rd way
# from package1.module1 import * #---4th way
# md.one()
# md.three()
# print(md.name)
# one()
# three()
# print(name)
# class Student:
#     name = "Rahul"
#     __id = 1001
#     def setName(self,name):
#         self.name = name
#     def getName(self):
#         return self.name
#     def setId(self,id):
#         self.__id = id
#     def getId(self):
#         return self.__id
# name = input("Enter name: ")
# id = int(input("Enter id: "))
# obj=Student()
# print("Before setter : ",obj.__dict__)
# obj.setName(name)
# print(obj.getName())
# obj.setId(id)
# print("After setter : ",obj.__dict__)
# print(obj.getId())
# import datetime
# def gettime():
#     return datetime.datetime.now()
# pin = '1001'
# balance = 50000
# # ask for pin
# entered_pin=input('Enter your pin : ')
# if pin==entered_pin:
#     #ask for deposit or withdrawal or mini statement
#     a=int(input("Press 1 for deposit,2 for withdrawal and 3 for mini statement : "))
#     if a==1:
#         deposit_amount = int(input("Enter amount for deposit : "))
#         if deposit_amount <=25000 and str(deposit_amount).endswith("00"):
#             with open("bank_statement.txt","a") as op:
#                 balance = balance + deposit_amount
#                 op.write(str([str(gettime())])+f"deposit : {deposit_amount} , Total Balance : {balance} \n")
#                 print("Amount deposit successfully")              
#             print("Total Balance : ",balance)

#         else :
#             print("You entered wrong amount please enter correct amount")

#     elif a==2:
#         withdrawal_amount = int(input("Enter amount for withdrawal : "))
#         if withdrawal_amount <=25000 and withdrawal_amount <= balance and str(withdrawal_amount).endswith("00"):
#             with open("bank_statement.txt","a") as op:
#                 balance = balance - withdrawal_amount
#                 op.write(str([str(gettime())])+f"withdrawal : {withdrawal_amount} , Total remaining Balance : {balance} \n")
#                 print("Amount withdrawal successfully")
#             print("Total remaining Balance : ",balance)
#         else :
#             print("You entered wrong amount please enter correct amount")
            
#     elif a==3:
#         print("Total Balance : ",balance)
# else:
#     print("pin is incorrect !")
# class PhonebookEntry:
#     def __init__(self, name, alias, number):
#         self.name = name
#         self.alias = alias
#         self.number = number
  

# class Phonebook:
#     def __init__(self):
#         self.entries = []
#     def add_entry(self, name, alias, number):
#         self.entries.append(PhonebookEntry(name, alias, number))
#     def display(self):
#         return self.entries
# p=PhonebookEntry("KL",1,123)
# p1=Phonebook()
# p1.add_entry("KL",1,123)
# res=p1.display()
# print(res)

# class Employee():
#     tasks = []
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#           # 👈️ initialize list

#     def add_task(self, task,task2):
#         Employee.tasks.append(task)
#         Employee.tasks.append(task2)


#         return Employee.tasks


# bob = Employee('Bobbyhadz', 100)

# res=bob.add_task('develop','ship')
# print(res)

# import re
# r=re.compile("\d+[a-z]")
# s="abc1234def4567abcd89"
# l=re.findall(r,s)
# print(l)

# class B(object):
#     def first(self):
#         print("first")
#     def second():
#         print("second")
# ob=B()
# B.first(ob)
# l1=[1,2,3]
# l2=[4,5,6]
# print([x*y for x in l1 for y in l2])


# def a(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return a(n-1)+a(n-2)

# for i in range(0,4):
#     print(a(i),end="")

# n=[1,2,3]
# a=list(filter(lambda x :(x+1)*3/3 %3==0,n))
# b=list(filter(lambda x :2,n))
# c=list(filter(lambda x :x==0,n))
# d=list(filter(lambda x :x>1,n))
# print(a)
# print(b)
# print(c)
# print(d)

# def foo():
#     t=t+1
#     return t
# t=0
# print(foo())
# l=[1,2,3,4]
# i=iter(l)
# while True:
#     try:
#         print(next(i),end="##")
#     except StopIteration:
#         break

# func=lambda x:return x
# kvps={"1":1,"2":2}
# thecopy=kvps
# kvps["1"]=5
# sum=kvps["1"]+thecopy["1"]
# print(sum)

# sum=0
# for i in range(4):
#     sum+=i
# print(sum)
# sum(34,23)
# def f(x):
#     def f1(a,b):
#         print("hello")
#         if b==0:
#             print("NO")
#             return
#         return f(a,b)
#     return f1

# @f
# def f(a,b):
#     return a%b
# f(4,0)
# d={"id":101,"name":"ABC"}
# a=d.setdefault("name","PQR")
# print(a)

# def outerFun(a,b):
#     def innerFun(c,d):
#         return c+d
#     return innerFun(a,b)
# res=outerFun(5,10)
# print(res)
# class Sales:
#     def __init__(self,id):
#         self.id=id
#         id=100
# val=Sales(123)
# print(val.id)

# i=0
# while i<3:
#     i=i+1
# print("i is",i)
# def even_in():
#     n=0
#     while True:
#         yield n
#         n=n+2
# ob=even_in()
# for i in range(2):
#     next(ob)
# print(next(ob))
x=[[0],[1]]
print(" ".join(list(map(str,x))))
# s="Python,Java,C,C++"
# print(s[10:1:-2])

# class A:
#     def test1(self):
#         print("A")

# class B(A):
#     def test(self):
#         print("B")

# class C(A):
#     def test(self):
#         print("C")

# class D(B,C):
#     def test2(self):
#         print("D")
# obj=D()
# obj.test()
# class fruits:
#     def __init__(self,price):
#         self.price=price
# obj=fruits(50)
# obj.quantity=10
# obj.bags=2
# print(obj.quantity+len(obj.__dict__))

# s="foobar"
# # print(s[::-1][::-5])
# # print(s[::-5])
# # print(s[0]+s[-1])
# print(s[::-5])
# t=[1,2,3,4,5]
# for i in t:
#     print(i,end="")
#     if i==2:
#         t.remove(i)

# def say(message,times=1):
#     print(message*times)
# say("Hello")
# say("World",5)