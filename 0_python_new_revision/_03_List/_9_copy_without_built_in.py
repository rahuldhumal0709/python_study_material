lst = [10,20,30,40,50]
lst2 = []
for i in range(len(lst)):
    lst2[i:i] = [lst[i]]
print('OG List : ',lst)
print('Copy : ',lst2)


