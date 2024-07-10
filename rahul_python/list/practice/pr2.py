inp=input("Enter input: ")
a1=[]
a1=inp.split()
a2=list(map(int,a1))
print(a2)

for i in range(len(a2)):
    for j in range(i+1,len(a2)):
        if a2[i]<a2[j]:
            a2[i],a2[j]=a2[j],a2[i]

print(a2)