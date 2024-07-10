# WAP to check if a given number is prime or not.
num = int(input("Enter a number: "))
flag = 0
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            flag = 1
            break
if flag==1:
    print("Given number is not a prime number")
else:
    print("Given number is a prime number")