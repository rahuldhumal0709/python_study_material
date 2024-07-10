# Q6.Python program to find out the average of a set of integers.

count = int(input("Enter the size of numbers : "))
i = 0
sum = 0
for i in range(count):
    x = int(input("Enter an element : "))
    sum = sum + x
avg = sum/count
print("The average is : ", avg)