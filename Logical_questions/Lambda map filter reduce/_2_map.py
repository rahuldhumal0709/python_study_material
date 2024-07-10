lst = [1,2,3,4,5]
#--------------------------------------------------------------1st way using normal function 
def square(lst):
    sq_lst = []
    for i in lst:
        sq = i ** 2
        sq_lst.append(sq)
    return sq_lst
square_lst = square(lst)
print(square_lst)
#--------------------------------------------------------------2nd way using map function
def square(lst):
    return lst ** 2
map_lst = list(map(square,lst))
print(map_lst)