#Ascending order
lst = [30, 20, 50, 25, 15, 70, 40]
print('Initial list : ',lst)
for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] > lst[j]:
            lst[i], lst[j] = lst[j], lst[i]
    # print(lst)
print('Ascending order list:', lst)

#Descending order
lst = [30, 20, 50, 25, 15, 70, 40]
# print(lst)
for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] < lst[j]:
            lst[i], lst[j] = lst[j], lst[i]
    # print(lst)
print('Descending order list:', lst)