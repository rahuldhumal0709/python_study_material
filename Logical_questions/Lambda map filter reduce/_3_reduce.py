from functools import reduce
#--------------------------------------------------------------In reduce fun 1st import reduce fun from functools module.
lst = [4,5,1,2,10,9,7,45]
#--------------------------------------------------------------1st way using Normal function 
def sum(lst):
    sums = 0
    for i in lst:
        sums += i
    return sums
result = sum(lst)
print(result)
#--------------------------------------------------------------2nd way using reduce function
def sum(lst,sums):
    return lst + sums
res = reduce(sum,lst)
print(res)