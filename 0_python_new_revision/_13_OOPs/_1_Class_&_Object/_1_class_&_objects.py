'''Class : 
--> It is a collection of objects.
--> A class is a blueprint for creating objects.
--> It defines a set of attributes and methods.
--> Attributes: Variables that belong to the class.
--> Methods: Functions defined inside a class.

Object : 
--> Object is instance of a class.
--> When a class is defined, no memory is allocated until an object of that class is created.
'''

class Calculator:
    def addition(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
        sum = num1 + num2
        return sum
    def subtraction(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
        sub = num1 - num2
        return sub
    def multiplication(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
        mul = num1 * num2
        return mul
    def division(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
        dev = num1 / num2
        return dev
    def modulus(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
        mod = num1 % num2
        return mod
obj = Calculator()
while(True):
    print('Which operation you want perform\n1.Addition\n2.Sutraction\n3.Multiplication\n4.Division\n5.Modulus\n6.Exit')
    op = int(input())
    if op==6:
        exit()
    elif op not in [1,2,3,4,5]:
        print('You entered wrong input')
        continue

    n1 = int(input("Enter number 1 : "))
    n2 = int(input("Enter number 2 : "))
    if op==1:
        result = obj.addition(n1,n2)
        print(f"Addition of {n1} and {n2} is : ",result)
    elif op==2:
        result = obj.subtraction(n1,n2)
        print(f"Subtraction of {n1} and {n2} is : ",result)
    elif op==3:
        result = obj.multiplication(n1,n2)
        print(f"Multiplication of {n1} and {n2} is : ",result)
    elif op==4:
        result = obj.division(n1,n2)
        print(f"Division of {n1} and {n2} is : ",result)
    elif op==5:
        result = obj.modulus(n1,n2)
        print(f"Modulus of {n1} and {n2} is : ",result)