# keys = [1,2,3,4,5]
# value = ['KL','MS','VK','RS','SR']
# dict1 = {k:v for k,v in zip(keys,value)}
# print(dict1)

# result = {keys[i]:value[j] for i in range(len(keys)) for j in range (i+1)}
# print(result)

# result1 = {keys[i]:value[i] for i in range(len(keys))}
# print(result1)

lst = [4,5,8,1,2,3]
# {4:[4,8,12.....40],5:[5,10,15,20,25,30....50]}

result = {lst[i]:[lst[i]*j for j in range(1,11)] for i in range (len(lst))}

print(result)