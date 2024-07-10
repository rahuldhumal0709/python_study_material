# Q11.Python program to find factorial of a given number.

num = int(input("Enter a number : "))
fact = 1
if num >= 0:
   for i in range(1,num + 1):
       fact = fact * i
   print(fact)
else:
   print("Negative input")