# Ask user for how many numeric item you want to add in lst and add those items.
lst = []
n = int(input('How many items you want to add in your list : '))
for i in range(n):
    item = int(input('Enter Item : '))
    lst.append(item)
print('Final list : ',lst)