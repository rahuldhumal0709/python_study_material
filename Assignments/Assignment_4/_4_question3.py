# Write a Python program to square the elements of a list using map() function.
lst = []
size=int(input("Size of list : "))
for i in range(size):
    ele=int(input())
    lst.append(ele)
def square(lst):
    return lst ** 2
lst1=list(map(square,lst))
print("Square the elements of the  : ",lst1)