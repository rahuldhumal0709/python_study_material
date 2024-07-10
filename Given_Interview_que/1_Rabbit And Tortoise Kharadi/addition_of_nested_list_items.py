sum=0
lst1=[1,2,3,4,[5,6,7],8,9]
for i in lst1:
    if type(i)==list:
        for j in i:
            sum=sum+j
    else:
        sum=sum+i
print(sum)