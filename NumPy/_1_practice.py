# NumPy is a Python library used for working with arrays.
# It also has functions for working in domain of linear algebra, fourier transform, and matrices.
# NumPy was created in 2005 by Travis Oliphant. It is an open source project and you can use it freely.
# NumPy stands for Numerical Python.
import numpy as np
print(np.__version__)

arr=np.array([1,2,3,4,5,6,7])   # Use List 1-D Array
print("\n1 - D Array",arr)
print(type(arr))

arr1 = np.array((1, 2, 3, 4, 5))    # Use Tuple 1-D Array
print("\n1 - D Array",arr1)
print(type(arr1))

arr2 = np.array(42)      # 0-D Array
print("\n0 - D Array",arr2)
print(type(arr2))

arr3 = np.array([[1, 2, 3], [4, 5, 6]])    # 2-D Array
print("\n2 - D Array",arr3)

arr4 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])  # 3-D Array
print("\n3 - D Array",arr4)