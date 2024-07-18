lst = []
n = int(input('How many item you want to add : '))
for i in range(n):
    item = int(input('Enter item : '))
    lst[i:i] = [item]
    print('Item added successfully')
print(lst)