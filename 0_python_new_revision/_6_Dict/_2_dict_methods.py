# dict_methods = dir(dict)
# lst = []
# for i in dict_methods:
#     if not str(i).startswith('__'):
#         lst.append(i)
# print(lst)

['items', 'keys','values','copy','clear','pop', 'popitem', 'get', 'update','setdefault', 'fromkeys']

dict1 = {'Name':'KL','Number':'1','DOB':'18-04-1992'}
for k,v in dict1.items():
    print(k,v)
print()
# ==============================================================
for k in dict1.keys():
    print(k)
print()
# ==============================================================
for v in dict1.values():
    print(v)
print()
# ==============================================================
dict2 = dict1.copy()
dict1.clear()
print('dict1 : ',dict1)
print('dict2 : ',dict2)
# ==============================================================

name = dict2["Name"] # Raises a KeyError if the key does not exist.
print("name : ",name) # Use when you are sure that the key exists in the dictionary.

# ==============================================================

get_name = dict2.get('Name') # Returns None or a specified default value if the key does not exist.
print("get_name : ",get_name) # Use when you are not sure if the key exists and you want to handle the missing key gracefully.

get_roll_no = dict2.get("Roll_no","47")
print("get_roll_no : ",get_roll_no)
print(dict2)
# ==============================================================

# setdefault : Get the value of a key and set it to a default value if the key does not exist.
name = dict2.setdefault('Name') # Key exists, returns the value
print("get name using setdefault : ",name)

set_defalt = dict2.setdefault("Roll_no","47")  # Key does not exist, sets the default value and returns it
print("set_defalt : ",set_defalt)
print(dict2)

# ==============================================================

# fromkeys : Create a new dictionary with specified keys and a common value.
keys = ['name', 'age', 'city']
new_dict = dict.fromkeys(keys, 'NA')
print('fromkeys : ',new_dict) 
# ==============================================================