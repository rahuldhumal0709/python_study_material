class Calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        sum = self.num1 + self.num2
        return sum
    def subtract(self):
        substraction = self.num1 - self.num2
        return substraction
    def multiply(self):
        multiplication = self.num1 * self.num2
        return multiplication
    def divide(self):
        division = self.num1 / self.num2
        return division
num1=int(input("Enter num1: "))
num2=int(input("Enter num2: "))
obj = Calculator(num1,num2)
print(obj.add())
print(obj.subtract())
print(obj.multiply())
print(obj.divide())