#find max number
l= []
for i in range(6):
    a=int(input("Enter a number="))
    l.append(a)
m=l[0]
for j in range(len(l)):
    if m<l[j]:
        m=l[j]
print(m)