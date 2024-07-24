# set comprehension - it is used to create a new set from another set/list/tuple

lst = [10,20,30,20,40,10,50,30,60,70,50,90,100]

# remove the duplicate from list using set comprehensions

# result = {i for i in lst}

# print(list(result))         # [100, 70, 40, 10, 50, 20, 90, 60, 30]

# set is unindex, unorder, no duplicates items

# =======================================================================

lst1 = ['A','b','C','d','E','f','C','h','I','J','K','I','L','m']

# Create a set accept only unique upper case letter from given lst

upper = {i for i in lst1 if i.isupper()}

print(upper)