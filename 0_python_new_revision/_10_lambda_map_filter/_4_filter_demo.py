'''
    filter() : 
        - It is used to filter items based on a specific condition and return a result list.
'''
lst = [3,4,2,5,7,6,8,1]
def even(data):
    lst = []
    for i in data:
        if i%2==0:
            lst.append(i)
    return lst
print(even(lst))

def even(data):
    return data%2==0
filter_item = list(filter(even,lst))
print(filter_item)

filter_lambda = list(filter(lambda lst:lst%2==0,lst))
print(filter_lambda)

# list_com = [i for i in lst if i%2==0]
# print(list_com)