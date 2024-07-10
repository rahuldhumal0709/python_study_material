from turtle import goto


lst =[2,3,4,5]
keys={}
for i in lst:
    values=[]
    for j in range(1,6):
        values.append(i*j)
        keys[i]=values
print(keys)

# dict1 = {i:[(i * j) for j in range(1,6)] for i in lst} 
# print(dict1)