# Q3.Python program to check whether given number is palindrome number or not.

num=int(input("Enter a number : "))
num1 = num
res=0
while num1 > 0:
   rem = num1 % 10
   res =rem + res * 10
   num1=num1//10    
if num == res:
   print("Given number is a palindrome number")
else:
   print("Given number is not a Palindrome number")