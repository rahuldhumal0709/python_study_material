lst = [10,4,6,1,7,8,9,11,56]
#--------------------------------------------------------------1st way using Normal normal method
lst1=[]
for i in range(len(lst)):
    if i%2 != 0:
        lst1.append(lst[i])
print(lst1)
#--------------------------------------------------------------2nd way using list comprehension
data=[lst[i] for i in range(len(lst)) if i%2!=0]
print(data)