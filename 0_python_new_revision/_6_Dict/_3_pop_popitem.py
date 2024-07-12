dict1 = {'Name':'KL','Number':'1','DOB':'18-04-1992'}

# Using pop to remove and return the value of Number
pop_number = dict1.pop('Number')
print('Number : ',pop_number)
print('dict1 : ',dict1)

# Does not return error if key is not present in dictionary
country = dict1.pop('country','Not found')
print('country : ',country)

# ===========================================================
dict1 = {'Name':'KL','Number':'1','DOB':'18-04-1992'}
print(dict1)

# Using popitem to remove last key-value-pair and return the pair.
pop_item = dict1.popitem()
print('pop_item : ',pop_item)
print('dict1 : ',dict1)

pop_item = dict1.popitem()
print('pop_item : ',pop_item)
print('dict1 : ',dict1)

pop_item = dict1.popitem()
print('pop_item : ',pop_item)
print('dict1 : ',dict1)
