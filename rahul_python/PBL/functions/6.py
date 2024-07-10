# Write a funtion that takes a number as a parameter checks whether the number is prime or not.
def primecheck(n):
    flag = 0
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                flag = 1
                break
    if flag==1:
        print(num, "is not a prime number")
    else:
        print(num, "is a prime number")
num=int(input())
primecheck(num)