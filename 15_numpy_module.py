# NUMPY:-
    # Numeric + Python  => Numpy

    # It is a powerful Python library used for:
            # Numerical Computation
            # Multi Diamensional Arrays
            # Matrix Operations
            # Scientific Computing
            # Data Analysis
            # Machine Learning

# l1 = [1, 2, 3, 4]    # one diamensional list
# l2 = [[1, 2], [3, 4]]  # two diamensional list
# l3 = [[[1, 2], [3, 4]], [[4, 5], [5, 6]]] # three diamensional list
# #==================================
# import numpy as np

    # Numpy is famous for creating N-diamensional Array

#-------------------------------------------

# Difference between an Array and List:

# List:
        # Collection datattype
        # Supports Indexing
        # Heterogeneous

# Array:
        # Collection Datatype
        # Supports Indexing
        # Homogeneous

# --------------------------
import numpy as np
# Creating Numpy Array:-

# arr1 = np.array([1, 2, 3, 4, 5])
# print(arr1)

# arr2 = np.array([1.1, 2.2, 3.3, 4.4, 5.5])
# print(arr2)

# arr3 = np.array([1, 2.2, 3, 4, 5])
# print(arr3)

# arr4 = np.array([1, "A", 2, 3, 4, 5])
# print(arr4)

# arr5 = np.array(["A", 5.5])
# print(arr5)

# arr6 = np.array(['1', 2, 3.3, "A"])
# print(arr6)

#----------------------------------------

# How to check type of an array:
# ar1 = np.array([1, 2, 3, 4, 5])
# print(ar1)
# print(type(ar1))   #<class 'numpy.ndarray'>

# How to check array Diamensions:

# ar2 = np.array(["A", "B", "C", "D", "E"])
# print(ar2)
# print(type(ar2))
# print(ar2.ndim) # 1

#-------------------------
# ar3 = np.array([
#     [1, 2, 3],
#     [4, 5, 6]
# ])
# print(ar3)
# print(type(ar3))
# print(ar3.ndim)  # 2

#--------------------------------

# ar4 = np.array([
#     [
#         [1, 2, 3],
#         [4, 5, 6]
#     ],
#     [
#         [6, 7, 8],
#         [9, 10, 11]
#     ]
# ])

# print(ar4)
# print(type(ar4))
# print(ar4.ndim)  #3

#---------------------------------

# Array Attributes:

# a1 = np.array([[1, 2, 3], [4, 5, 6]])
# print(a1)
# print(type(a1))
# print(a1.ndim)  # to check diamensions of an array
# print(a1.shape) # to know the no. of rows and no. of cols 
# print(a1.size)  # to know total count of elements
# print(a1.dtype) # to know the elements data type

#-------------------------------

# Some Special Arrays:

# Zeros Array:

# ar1 = np.array([0, 0, 0, 0, 0])
# print(ar1)

# zeros1 = np.zeros((2, 3))
# print(zeros1)

# print("---------------")

# zeros2 = np.zeros((4, 2))
# print(zeros2)


#----------------------

# Ones Array:

# ones1 = np.ones((5, 5))
# print(ones1)

# print("-----------------")

# ones2 = np.ones((5, 20))
# print(ones2)

#------------------------------

# Identity Matrix:
# identity1 = np.eye(3)
# print(identity1)

# identity2 = np.eye(10)
# print(identity2)
#--------------------------------

# Range Array:

# ar1 = np.arange(1, 10)   
# print(ar1)   #[1 2 3 4 5 6 7 8 9]

# create an 1D array of all even numbers in between 20 to 50
# ar2 = np.arange(20, 50, 2)
# print(ar2)   #[20 22 24 26 28 30 32 34 36 38 40 42 44 46 48]

# np.arange(1, 10, 2)


#----------------------
# Evenly spaced Values

# linspace

# arr1 = np.linspace(1, 10, 25)
# print(arr1)

# arr2 = np.linspace(5, 6, 10)
# print(arr2)

#--------------------------

# Array Indexing:

# arr100 = np.array([10, 20, 30, 40, 50])
# print(arr100)

# print(arr100[2])
# print(arr100[-3])


# arr200 = np.array([
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ])
# print(arr200[0])
# print(arr200[-3])
# print(arr200[0][0])

# print(arr200[0, 0])
# print(arr200[1, 1])
# print(arr200[1, 2])

# print(arr200)
# print(type(arr200))
# print(arr200.ndim)   #2
# print(arr200.shape)
# print(arr200.size)
# print(arr200.dtype)

#----------------------------------

# SLICING:-

# arr1000 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# print(arr1000[2:6])

# 8 5 2
# print(arr1000[-3::-3])

# Mathematical Operations :

# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])

# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a // b)
# print(a % b)

#---------------------
# array:

# print(np.array((12, 23, 34, 45)))
# print(np.array({100, 200, 300, 400, 200, 100}))


# arange:
# print(np.arange(1, 10, 2))

# linspace:
# print(np.linspace(0, 100, 5))

# zeros:
# print(np.zeros((2, 3)))

# ones:
# print(np.ones((4, 5)))

# reshape:
# arr = np.arange(12)
# print(arr)

# reshaped = arr.reshape((3, 4))
# print(reshaped)

# sum:
# arr1 = np.array([10, 20, 30])
# print(np.sum(arr1))

# arr2 = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# arr3 = np.array(arr2)
# print(np.sum(arr3))


# mean:
# arr = np.array([10, 20, 30, 40])
# print(arr.mean())

# max:
# print(np.max(arr))

# min:
# print(np.min(arr))

# where:  It returns indexes where condition is true
# arr1 = np.array([10, 20, 30, 40, 50])
# result = np.where(arr1 > 25)
# print(result)


# Replace values conditionaly

# arr2 = np.array([10, 20, 30, 40, 50])
# result = np.where(arr2 > 25, "Pass", "Fail")
# print(result)

# unique:  removes duplicates and it sorts:
# arr3 = np.array([1, 2, 2, 3, 4, 4, 4, 5, 6, 1, 0, 7])
# print(np.unique(arr3))

# sort: sorts elements

# arr4 = np.array([50, 30, 20, 20, 10, 70, 25])
# print(np.sort(arr4))

# Generate random floats between 0 and 1

# arr5 = np.random.rand(5)
# print(arr5)

# arr6 = np.random.rand(2, 3)
# print(arr6)


#---------------------
# random integers
# arr7 = np.random.randint(1, 10, size=5)
# print(arr7)

# arr8 = np.random.randint(low=5, high=20, size=(2, 5))
# print(arr8)


#-------------------
# Dot Product / Matrix Multiplication 
# dot:

# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])

# print(np.dot(a, b))


# p = np.array([
#     [1, 2],
#     [3, 4]
# ])

# q = np.array([
#     [5, 6],
#     [7, 8]
# ])

# print(np.dot(p, q))

#-------------
# matrix inverse
# linalg:

# A = np.array([
#     [1, 2],
#     [3, 4]
# ])

# print(np.linalg.inv(A))
# print(np.linalg.