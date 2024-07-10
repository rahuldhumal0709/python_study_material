# Enter number : 5
# [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]

inp=int(input("Enter number : "))
r=inp**2
lst=[]
for i in range(inp):
    lst1=[]
    for j in range(inp):
        lst1.insert(0,r)
        r=r-1
    lst.insert(0,lst1)
print(lst)
