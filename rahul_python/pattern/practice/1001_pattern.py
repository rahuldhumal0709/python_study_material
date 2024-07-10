r=int(input("Enter row size :"))
c=int(input("Enter column size :"))
for i in range(1,r+1):
    for j in range(1,c+1):
        if(i==1 or j==1 or i==r or j==c):
            print("1",end=" ")
        else:
            print("0",end=" ")
    print()
print()

for i in range(1,r+1):
    for j in range(1,c+1):
        if(i==j):
            print("1",end=" ")
        else:
            print("0",end=" ")
    print()