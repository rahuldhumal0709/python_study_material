# Write a Python program to create a lambda function that adds 25 to a given number passed in as an argument.
num=int(input())
sum = lambda num : num + 25
print(sum(num))