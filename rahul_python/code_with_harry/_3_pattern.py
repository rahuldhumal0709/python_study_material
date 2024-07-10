n=int(input("Enter range : "))
b=int(input("Type 1 or 0 : "))
b1=bool(b)
if b1==True:
    for i in range(0,n):
        for j in range(0,i+1):
            print("*",end=" ")
        print()
else:
    for i in range(n,0,-1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()