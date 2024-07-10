l= []
for i in range(6):
    a=int(input("Enter a number="))
    l.append(a)
b=0
for j in range(len(l)):
    b=l[j]+b
print(b)