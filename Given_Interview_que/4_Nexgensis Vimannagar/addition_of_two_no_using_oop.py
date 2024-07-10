class Addition:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def output(self):
        return self.num1 + self.num2
n1=int(input("Enter first number : "))
n2=int(input("Enter second number : "))
A=Addition(n1,n2)
sum=A.output()
print(sum)