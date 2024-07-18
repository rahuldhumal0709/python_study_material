lst = [4,1,3,2,9,6,7,5]

for i in range(len(lst)):
    for j in range(i+1,len(lst)):
        if lst[i] < lst[j]:
            lst[i], lst[j] = lst[j], lst[i]
print(lst)
print(f'Max number in given list is : {lst[0]}\nSecond max number in given list is : {lst[1]}')
# print(f'Min number in given list is : {lst[-1]}\nSecond min number in given list is : {lst[-2]}')