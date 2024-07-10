# Write a function to calculate and return the factorial of a given number(a non-negative integer).
def factorial(num):
    fact = 1
    if num >= 0:
        for i in range(1,num + 1):
            fact = fact * i
        return fact
n=int(input())
print(factorial(n))