l1=[1,3,5,7,9]
l2=[2,4,6,8,10]
index=0
for i in range(1,11,2):
    l1.insert(i,l2[index])
    index=index+1
print("Combine list : ",l1)