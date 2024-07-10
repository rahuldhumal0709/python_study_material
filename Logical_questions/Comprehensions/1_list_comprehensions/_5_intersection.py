lst1 = [1,2,3,4,5]
lst2 = [4,5,6,7,8]
#--------------------------------------------------------------1st way using Normal normal method
lst3=[]
for i in lst1:
    for j in lst2:
        if i==j:
            lst3.append(i)
print(lst3)
#--------------------------------------------------------------2nd way using list comprehension
data = [i for i in lst1 for j in lst2 if i==j]
print(data)