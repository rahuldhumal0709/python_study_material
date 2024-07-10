# Write a Python program to count the number of even and odd numbers from a series of numbers.
size=int(input("Size of list : "))
numbers = []
for i in range(0,size):
   ele=int(input(""))
   numbers.append(ele)
even = 0
odd = 0
for i in numbers:
    if((i % 2)==0):
        even = even + 1
    else:
        odd = odd + 1
print("Number of even numbers : ",even)
print("Number of odd numbers : ",odd)