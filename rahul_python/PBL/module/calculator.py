import math_module
print('Enter 1 for addition')
print('Enter 2 for substraction')
print('Enter 3 for multiplication')
print('Enter 4 for divition ')
n= int(input() )
num1=int(input('enter first number: '))
num2=int(input('enter second number: '))
if n==1:
  math_module.add(num1,num2)
elif n==2:
    math_module.sub(num1,num2)
elif n==3:
    math_module.mul(num1,num2)
elif n==4:
    math_module.div(num1,num2)
else:
    print ('invalid input')