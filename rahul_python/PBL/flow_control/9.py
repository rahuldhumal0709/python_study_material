# WAP to print the reverse of a given number.
num=int(input("Enter a number : "))
res=0
while num > 0:
   rem = num % 10
   num = num//10
   res =rem + res * 10
print(res)