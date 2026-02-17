import numpy as np

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
matrix = np.random.randint(0,13,size=(3,4))
print(f"Matrix {matrix}")
print(f"First 2 rows = {matrix[:2,:]}")
print(f"Last 2 cols = {matrix[:,:-2]}")


#Question 7
arr = np.random.randint(-10,11,size=10)
print(f"Original array: {arr}")
# Replace negative numbers with 0
arr[arr < 0] = 0
print(f"After replacing negatives with 0: {arr}")


#Question 8
matrix_a = np.array([
    [1,2,3],
    [4,5,6]
])
matrix_b = np.array([
    [7,8,9],
    [10,11,12]
])
print(f"Original Matrix A - {matrix_a} and B - {matrix_b}")
# Vertical (stack rows) - axis=0
print(f"Result of concatenating Vertically - {np.concatenate((matrix_a,matrix_b),axis=0)}")
# Horizontal (stack columns) - axis=1
print(f"Result of concatenating Vertically - {np.concatenate((matrix_a,matrix_b),axis=1)}")

#Question 9

arr = np.random.rand(100)
indices = np.where(arr > 0.8)[0]  # [0] extracts from tuple
print(indices)  # e.g., [1, 4, 8, 15, ...]


#Question 10
matrix = np.random.randint(1,20,size=(4,4))

print(f"Matrix - {matrix}")
print(f"Row wise Addition - {matrix.sum(axis=1)}")# Sum ACROSS rows (each column)
print(f"Column wise Addition - {matrix.sum(axis=0)}") # Sum ACROSS columns (each row)

