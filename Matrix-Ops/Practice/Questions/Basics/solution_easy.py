import numpy as np
from numpy.ma.core import identity

rows = 4
cols = 4
matrix_4 = np.random.randint(0,101,size=(rows,cols))
print(f"Matrix  - {matrix_4}")
print(f"Shape - {np.shape(matrix_4)}")
print(f"Dimensions - {matrix_4.ndim}")


#Question 2
rows = 3
cols = 5
arr = np.linspace(0,5,15)
matrix = arr.reshape(rows,cols)
print(f"Reshaped Matrix - {matrix}")


#Question 3
rows = 1
cols = 6
matrix_1 = np.random.randint(1,100,size=(rows,cols))
matrix_2 = np.random.randint(1,100,size=(rows,cols))

print(f"Matrix Op")
print(f"Addition = {matrix_1 + matrix_2}")
print(f"Subtraction = {matrix_1 - matrix_2}")
print(f"Multiplication  = {matrix_1  * matrix_2}")
print(f"Division  = {matrix_1 / matrix_2}")


#Question 4
rows = 5
cols = 5
identity_matrix = np.eye(5)
print(f"Identity Matrix - {identity_matrix}")
identity_matrix[-1:]=7
print(f"After last row  7  - {identity_matrix}")


#Question 5
arr = np.random.randint(1,101,20)
print(f"Arr - {arr}")
print(f"Mean - {np.mean(arr)}")
print(f"Median - {np.median(arr)}")
print(f"Standard Deviation - {np.std(arr)}")
print(f"Variance - {np.var(arr)}")


#Question 6
rows = 3
cols = 4
matrix = np.random.randint(0,13,size=(rows,cols))
print(f"Matrix {matrix}")
print(f"First 2 rows = {matrix[:2,:]}")
print(f"Last 2 cols = {matrix[:,:-2]}")