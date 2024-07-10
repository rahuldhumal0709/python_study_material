# WAP to find if the given number is palindrome or not.
num=int(input("Enter a number : "))
num1 = num
res=0
while num1 > 0:
   rem = num1 % 10
   res =rem + res * 10
   num1=num1//10    
if num == res:
   print(num,"is a Palindrome.")
else:
   print(num,"is not a Palindrome.")