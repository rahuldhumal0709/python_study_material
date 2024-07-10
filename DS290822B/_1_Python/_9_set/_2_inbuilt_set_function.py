set_demo = set({1,2,3})
print(set_demo, type(set_demo))

set_demo1 = {1,2,3,5,10,4,6,7}
print("OG : ",set_demo1,type(set_demo1))

# set_demo.add(200)
# print("Add : ",set_demo)

# set_demo1.remove(10)
# print("Remove : ",set_demo1)

# set_demo1.discard(11)
# print("Discard : ",set_demo1)

# set_copy = set_demo.copy()
# print("Copy : ",set_copy)

# set_clear = set_demo.clear()
# print("Clear : ",set_clear)
# print("Copy : ",set_copy)

# for i in set_copy:
#     print(i)

set1 = {10,1,8,9,7,11,100,15,21}
set2 = {1,10,9,7,11,15,20,19}

# set3 = set1.difference(set2) # set1 - set2
# print("Difference : ",set3)

# set1.difference_update(set2)
# print("Difference Update : ",set1)

# set3 = set1.intersection(set2)
# print("Intersection : ",set3)

# set1.intersection_update(set2)
# print("Intersection Update : ",set1)

set1={1,2,3}
set2={1,2,3,4}

set3 = set1.union(set2)
print("Union : ",set3)

set3 = set1.issuperset(set2) # it is checking if all the elements of set2 is present inside set1 or not
print("Issuperset : ",set3)

set3 = set1.issubset(set2) # it is checking if all the elements of set1 is in set2
print("Issubset : ",set3)
