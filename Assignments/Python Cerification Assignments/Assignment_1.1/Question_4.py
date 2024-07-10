# Q4.Python program to check whether given number is Armstrong or not.

num=int(input("Enter a number : "))
order = len(str(num))
num1 = num
res=0
while num1 > 0:
   rem = num1 % 10
   res =res + rem ** order
   num1=num1//10
if num == res:
   print("Given number is an Armstrong number")
else:
   print("Given number is a not an Armstrong number")