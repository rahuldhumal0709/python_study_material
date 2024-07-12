# Set: set(), {}
# --> Set is a data structure in python it is used to store multiple items in a single variable.
# --> It is mutable
# --> unordered, Iterable, Non-Indexed
# --> Not allow duplicate items
# --> Allow heterogeneous data

set_methods = dir(set)
lst = []
for i in set_methods:
    if not str(i).startswith('__'):
        lst.append(i)
print(lst)