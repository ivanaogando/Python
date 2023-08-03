"""
work_with_python.py

Project: None

Maintainer Ivana Ogando González (you@you.you)
Created @ Wednesday, 2nd August 2023 12:14:36 pm

Copyright (c) 2023 Your Company
All Rights Reserved
"""

import numpy as np

# #################### Python For Data Science Cheat Sheet ####################

# ##### Creating Arrays #####
# 1D
d1 = np.array([1, 2, 3])
print(d1)
# 2D
d2 = np.array([(1, 2, 3), (4, 5, 6)], dtype=float)
print("\n", d2, "\n")
# 3D
d3 = np.array([[(1.5, 2, 3), (4, 5, 6)], [(3, 2, 1), (4, 5, 6)]], dtype=float)
print(d3)

# ---------------------------- Initial Placeholders ----------------------------

# Create an array of zeros, with 3 rows and 4 columns
a = np.zeros((3, 4))
print("\n", a)
# Create an array of ones, 2D with 3 rows and 4 columns
b = np.ones((2, 3, 4), dtype=np.int16)
print("\n", b)
# Create an array of evenly spaced values (step value), from 10 (included) up to
# 25 (not included), each 5: 10-15-20
c = np.arange(10, 25, 5)
print("\n", c)
# Create an array of evenly spaced values (number of samples), 9 numbers from
# 0 to 2 (both included)
d = np.linspace(0, 2, 9)
print("\n", d)
# Create a constant array, of 2 rows and 2 columns whose value is 7
e = np.full((2, 2), 7)
print("\n", e)
# Create a 2X2 identity matrix, of 2 rows and 2 columns, with opposed values as
# a mirror
f = np.eye(2)
print("\n", f)
# Create an array with random values, of 2 rows and 2 columns, with random values
g = np.random.random((2, 2))
print("\n", g)
# Create an empty array, with 3 rows and 2 columns
h = np.empty((3, 2))
print("\n", h)

# ------------------------------------ I/O -------------------------------------

# Saving & Loading On Disk
np.save("my_array", d1)
np.savez("array.npz", d2, d3)
np.load("my_array.npy")
# Saving & Loading Text Files
# np.loadtxt("myfile.txt")
# np.genfromtxt("my_file.csv", delimiter=',')
# np.savetxt("myarray.txt", d1, delimiter=" ")

# --------------------------------- Data Types ---------------------------------

# Signed 64-bit integer types
# np.int64
# Standard double-precision floating point
# np.float32
# Complex numbers represented by 128 floats
# np.complex
# Boolean type storing TRUE and FALSE values
# np.bool
# Python object type
# np.object
# Fixed-length string type
# np.string_
# Fixed-length unicode type
# np.unicode_

# ------------------------------- Asking For Help ------------------------------

np.info(np.ndarray.dtype)

# ------------------------------ Array Mathematics -----------------------------

# ----- Arithmetic Operations -----
# Subtraction
print("\n", d1 - d2)
print("\n", np.subtract(d2, d1))
# Addition
print("\n", d1 + d2)
print("\n", np.add(d1, d2))
# Division
print("\n", d1 / d2)
print("\n", np.divide(d1, d2))
# Multiplication
print("\n", d1 * d2)
print("\n", np.multiply(d1, d2))
# Exponentiation
print("\n", np.exp(d2))
# Square root
print("\n", np.sqrt(d2))
# Print sines of an array
print("\n", np.sin(d1))
# Element-wise cosine
print("\n", np.cos(d2))
# Element-wise natural logarithm
print("\n", np.log(d1))
# Dot product
print("\n", e.dot(f))

# ----- Comparison -----
# Element-wise comparison
print("\n", d1 == d2)
print("\n", d1 < 2)
# Array-wise comparison
print("\n", np.array_equal(d1, d2))

# ----- Aggregate Functions -----
# Array-wise sum
print("\n", d1.sum())
# Array-wise minimum value
print("\n", d1.min())
# Maximum value of an array row
print("\n", d2.max(axis=0))
# Cumulative sum of the elements
print("\n", d2.cumsum(axis=1))
# Mean
print("\n", d1.mean())
# Median
print("\n", np.median(d2))
# Correlation coefficient
print("\n", np.corrcoef(d2))
# Standard deviation
print("\n", np.std(d2))

# -------------------------------- Copying Arrays ------------------------------

# Create a view of the array with the same data
i = d1.view()
print("\n", i)
# Create a copy of the array
print("\n", np.copy(d1))
# Create a deep copy of the array
i = d1.copy()
print("\n", i)

# -------------------------------- Sorting Arrays ------------------------------
# Sort an array
print("\n", d1.sort())
# Sort the elements of an array's axis
print("\n", d3.sort(axis=0))

# ------------------------ Subsetting, Slicing, Indexing -----------------------
# ----- Subsetting -----
# Select the element at the 2nd index
print("\n", d1[2])
# Select the element at row 1 column 2 (equivalent to b[1][2])
print("\n", d2[1, 2])

# ----- Slicing -----
# Select items at index 0 and 1
print("\n", d1[0:2])
# Select items at rows 0 and 1 in column 1
print("\n", d2[0:2, 1])
# Select all items at row 0 (equivalent to b[0:1, :])
print("\n row 0", d2[:1])
# Select all items at column 0
print("\n row 1", d2[1:])
# Same as [1,:,:]
print("\n", d3[1, ...])
# Reversed array a
print("\n", d1[::-1])

# ----- Boolean Indexing -----
# Select elements from a less than 2
print("\n", d1[d1 < 2])

# ----- Fancy Indexing -----
# Select elements (1,0),(0,1),(1,2) and (0,0)
print("\n", d2[[1, 0, 1, 0], [0, 1, 2, 0]])
# Select a subset of the matrix's rows and columns
print("\n", d2[[1, 0, 1, 0]][:, [0, 1, 2, 0]])

# ------------------------------ Array Manipulation ----------------------------

# ----- Transposing Array -----
# Permute array dimensions
print("\n", np.transpose(d2))
print("\n", d2.T)

# ----- Changing Array Shape -----
# Flatten the array
print("\n", d2.ravel())

# Reshape, but don't change data
print("\n", g.reshape(-3, 2))

# ----- Adding/Removing Elements -----
# Return a new array with shape (2,6)
print("\n", h.resize((2, 6)))

# Append items to an array
print("\n", np.append(h, g))

# Insert items in an array
print("\n", np.insert(a, 1, 5))

# Delete items from an array
print("\n", np.delete(a, [1]))

# ----- Combining Arrays -----
# Concatenate arrays
print("\n", np.concatenate((d1, d), axis=0))
# Stack arrays vertically (row-wise)
print("\n", np.vstack((d1, d2)))
# Stack arrays vertically (row-wise)
print("\n", np.r_[e, f])
# Stack arrays horizontally (column-wise)
print("\n", np.hstack((e, f)))
# Create stacked column-wise arrays
# print("\n", np.column_stack((d1,d)))
# Create stacked column-wise arrays
# print("\n", np.c_[d1,d])
# ----- Splitting Arrays -----
# Split the array horizontally at the 3rd index
print("\n", np.hsplit(d1, 3))
# Split the array vertically at the 2nd index
print("\n", np.vsplit(d3, 2))
