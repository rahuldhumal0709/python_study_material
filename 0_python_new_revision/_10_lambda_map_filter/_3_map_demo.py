'''
    map() : 
        - The map() function is used to apply a function to each item in an iterable.
        - When we perform an operation on each item in a list, we use the map function.
'''

lst = [4,5,1,2,10,9,7,45]
# =========================================
#Using Normal Funtion
def square(data):
    sq_lst = []
    for i in data:
        sq = i ** 2
        sq_lst.append(sq)
    return sq_lst
square_lst = square(lst)
print(square_lst)
# =========================================
#Using Normal Funtion with map
def square(data):
    return data ** 2
square_lst = list(map(square,lst))
print(square_lst)
# =========================================
#Using lambda Funtion with map
sq_list=list(map(lambda lst:lst**2,lst))
print(sq_list)
# =========================================
# Using list comprehensions
sq = [i**2 for i in lst]
print(sq)