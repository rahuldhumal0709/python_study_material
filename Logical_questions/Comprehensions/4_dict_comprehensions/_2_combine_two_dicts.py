keys = [1,2,3,4,5]
values = [10,20,30,40,50]
res = {}
for k in keys:
    for v in values:
        res[k]=v
        values.remove(v)
        break
print(res)
#------------------------------------------------------using zip method
keys = [1,2,3,4,5]
values = [10,20,30,40,50]
dict = {k:v for k,v in zip(keys,values)}
print(dict)
#------------------------------------------------------using dict comprehension
dict1={keys[i]:values[i] for i in range (len(keys))}
print(dict1)