'''
    reduce() :
        - It is used to perform an operation on all items in a list and return a single result.
        - The reduce() function is imported from the 'functools' module.
'''

from functools import reduce

lst = [10,20,30,40,10]
def sum(data):
    sum = 0
    for i in data:
        sum = sum + i
    return sum
print(sum(lst))

def sum(data1,data2):
    return data1+data2
sum_res = reduce(sum,lst)
print(sum_res)

lst = [10,20,30,40,10]
result = reduce(lambda data1,data2:data1+data2,lst)
print(result)