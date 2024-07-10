lst = [5,6,3,1,3,5,2,4]
print(lst)
lst1 = []
for i in lst:
    count = lst.count(i)
    if count == 1:
        lst1.append(i)
print(lst1)