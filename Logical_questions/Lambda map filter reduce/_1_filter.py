lst = [4,5,61,2,8,10,11]
#--------------------------------------------------------------1st way using Normal function 
def even(lst):
    """This is a function which will return even numbers from given list""" # doc string whithin a function
    even_lst = []
    for i in lst:
        if i%2==0:
            even_lst.append(i)
    return even_lst
elst = even(lst)
print(even.__doc__) #------------------------------------------print doc string
print(elst)
#--------------------------------------------------------------2nd way using filter function
def even(lst):
    return lst%2==0
fil_lst = list(filter(even,lst))
print(fil_lst)