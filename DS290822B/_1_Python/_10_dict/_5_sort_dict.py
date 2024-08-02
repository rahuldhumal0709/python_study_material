dict1 = {208:"Rahul",109:"Vishal",111:"Dipak"}
keys = []
for i in dict1.keys():
    keys.append(i)
print(keys)
for i in range(len(keys)):
    for j in range(i+1,len(keys)):
        if keys[i] > keys[j]:
            keys[i],keys[j] = keys[j],keys[i]
dict1 = {i:dict1[i] for i in keys}
print(dict1)
