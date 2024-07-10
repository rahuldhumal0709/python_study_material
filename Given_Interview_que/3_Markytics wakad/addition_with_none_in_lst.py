lst=[1,2,3,None]
sum=0
for i in lst:
    if i==None:
        continue
    else:
        sum=sum+i
print(sum)