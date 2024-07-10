a=int(input(""))
b=int(input(""))
s1=0
s2=0
for i in range(0,a):
    t1=float(input(""))
    s1=s1+t1
for j in range(0,b):
    t2=float(input(""))
    s2=s2+t2
total=(s1*18)+(s2*12)
print("Total estimated is :",total,"INR")