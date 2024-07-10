# Write a Python program to triple all numbers of a given list of integers. Use Python map.
lst=[]
size=int(input("Size of list : "))
for i in range(size):
    ele=int(input())
    lst.append(ele)
def triple(lst):
    return lst * 3
lst1 = list(map(triple,lst))
print("Triple of list numbers : ",lst1)