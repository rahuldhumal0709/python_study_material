# set1 = {1, 2, 3}
# set2 = {1, 2, 3, 4, 5}
# set3 = {1, 2}

# Check if set1 is a subset of set3
# is_sub = set1.issubset(set2)
# print(is_sub)  # Output: True

# # Check if set2 is a subset of set1
# is_sub = set2.issubset(set1)
# print(is_sub) # Output: False

# # Check if set3 is a subset of set1
# is_sub = set3.issubset(set1)
# print(is_sub) # Output: True

# =========================================================
#Superset
set1 = {1, 2, 3, 4, 5}
set2 = {1, 2, 3}

is_super = set1.issuperset(set2)
print(is_super)  # Output: True

is_super = set2.issuperset(set1)
print(is_super)  # Output: False
