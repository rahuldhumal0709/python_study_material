n=int(input("How many terms? "))
n1, n2 = 0, 1
count = 0
if n >= 0:
   print("Fibonacci sequence:")
   while n > count:
       print(n1,end=" ")
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count = count + 1
else:
   print("Please enter a positive integer")
   
# Print the nth fibonacci number
# def Fibonacci(n):
#     if n<= 0:
#         return "Incorrect input"
#     elif n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         return Fibonacci(n-1)+Fibonacci(n-2)
 
# n=int(input("Enter input : "))
# print(Fibonacci(n))