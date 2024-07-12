# Get a key and value from user and print
n = int(input('How many records you want to get : '))
dict1 = {}
for i in range(n):
    key = input('Enter key : ')
    value = input('Enter value : ')
    dict1[key]=value
print(dict1)