for i in range(4,0,-1):
    for k in range(i,4):
        print(end="  ")
    for j in range(i,0,-1):
        print(j,end=" ") #4321 321 21 1
    for n in range(2,i+1):
            print(n,end=" ") #234 23 2
    print()
    