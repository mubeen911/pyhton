import numpy as np
#creating a 1D array
arr= np.array([1,2,3,4,5])
# print(arr)


a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
#3D array
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

#print(c)
# shape tells the each  dimension elements means how many values dimension have
# print('shape of array :', c.shape)
# print(a.ndim)
# print(b.ndim)
# print(c.ndim)
# print(d.ndim)

# changing the dimension of array using reshape
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(4, 3)

#print(newarr)


# split array into  four parts using split function
newarr = np.array_split(arr, 4)

# print(newarr)

# search for numbers in array using sort function
arr = np.array([3, 2, 0, 1])

#print(np.sort(arr))

#creating random number for numpy
from numpy import random

x = random.randint(100)

print(x)