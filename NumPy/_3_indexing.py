import numpy as np
# Access 1-D Arrays
# arr = np.array([1, 2, 3, 4])
# print(arr[0])
# print(arr[2] + arr[3])

# Access 2-D Arrays
# arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
# print('2nd element on 1st row: ', arr[0, 1])
# print('5th element on 2nd row: ', arr[1, 4])
# print(arr.shape)
# print(arr.dtype)

# Access 3-D Arrays
# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# print(arr[0, 1, 2])
# print(arr.shape)

# Negative Indexing
# arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
# print('Last element from 2nd dim: ', arr[1, -1])

# ide=np.identity(5)
# print(ide)
# print(ide.shape)

l1 = [[1,2,3],[4,5,6]]
arr = np.array(l1)
l2 = []
for list1 in arr:
    l2.extend(list1)
print(l2)
