array=[1,25,8,10,30,40,70,100,85]
n=15
lst=[]
for i in range(len(array)):
    for j in range(len(array)):
        if (array[i]-array[j])==n:
            new_lst=[]
            new_lst.extend([array[i],array[j]])
            lst.append(new_lst)
print(lst)