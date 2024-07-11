# Ask user for how many item you want to add in lst and then ask for data type also and add those items.
lst = []
n = int(input('How many items you want to add in your list : '))
for i in range(n):
    dt = int(input('Enter datatype\n1.int\n2.string\n3.float\n4.boolean\n'))
    if(dt==1):
        item = int(input(f'Enter int item index {i} : '))
    elif(dt==2):
        item = input(f'Enter string item index {i} : ')
    elif(dt==3):
        item = float(input(f'Enter float item index {i} : '))
    elif(dt==4):
        item = bool(input(f'Enter boolean item index {i} : '))
    else:
        print('You entered wrong input')
        break
    lst.append(item)
    print('Item added successfully\n')
print('Final list : ',lst)
print('Thank you')
