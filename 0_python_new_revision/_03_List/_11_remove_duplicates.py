l = [2,3,4,2,5,6,3,4,7]
lis = []
for i in l:
    if i not in lis:
        lis[i:i] = [i]
print(lis)