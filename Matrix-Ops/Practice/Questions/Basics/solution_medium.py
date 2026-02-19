import math

import numpy as np

#Question 11
rows = 3
cols = 3
matrix_1 = np.random.randint(1,20,size=(rows,cols))
matrix_2 = np.random.randint(1,20,size=(rows,cols))
resultant_matrix = matrix_1 @ matrix_2
print(f"Matrix  multiplication  - {resultant_matrix}")
print(f"Determinant - {np.linalg.det(resultant_matrix)}")


#Question 12
rows = 10
cols = 10

arr  = np.random.rand(rows,cols)
bin_arr = np.where(arr > 0.5,1,0)
#Alternate
#binary_arr = (arr > 0.5).astype(int)
print(f"Binary = {bin_arr}")

#Question 13

def is_prime(n):
    if n < 2:
        return False
    for _ in range(2,int(n ** 0.5)+1):
        if n % _ == 0:
            return False
    return True

arr = np.random.randint(0, 101, size=50)
print(f"Original array:\n{arr}")

# Find prime numbers and replace with -1
primes_mask = np.vectorize(is_prime)(arr) #Apply function to entire array
arr[primes_mask] = -1

print(f"\nArray after replacing primes with -1:\n{arr}")


#Question 14

def square(n):
    return math.pow(n,2)
rows = 5
cols = 5
matrix = np.random.randint(1,20,size=(rows,cols))
print(f"Matrix - {matrix}")
diagonal_elements = np.linalg.diagonal(matrix)
squared = np.vectorize(square)(diagonal_elements)
print(f"Diagonal Elements  - {diagonal_elements}")
print(f"Squared Elements  - {squared}")


#Question 15
matrix_a = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

matrix_b = np.array([
    [1],
    [2],
    [3]
])
resultant_matrix = matrix_a + matrix_b
print(f"Matrix - {matrix_a}")
print(f"Result - Broadcasting  - {resultant_matrix}")


#Question 16
A = np.random.randint(1,100,size=(8,8))
print(f"Matrix - {A}")

# Method 1: Using np.argpartition (efficient for large arrays)
# Get flat indices of 5 largest values
flat_indices = np.argpartition(A.ravel(), -5)[-5:]

# Sort them to get descending order
flat_indices = flat_indices[np.argsort(A.ravel()[flat_indices])][::-1]

# Convert flat indices to 2D row, col indices
rows, cols = np.unravel_index(flat_indices, A.shape)

print("5 Largest Values and Their Positions:")
for i, (r, c) in enumerate(zip(rows, cols)):
    print(f"  Rank {i+1}: Value {A[r, c]} at position ({r}, {c})")

print()
# Method 2: Using np.argsort (simpler, good for small arrays)
flat_sorted = np.argsort(A, axis=None)[-5:][::-1]
rows2, cols2 = np.unravel_index(flat_sorted, A.shape)

print("Verification (using argsort):")
for r, c in zip(rows2, cols2):
    print(f"  Value {A[r, c]} at ({r}, {c})")



#Question 17
def moving_average_convolve(array, window_size):
    weights = np.ones(window_size) / window_size
    return np.convolve(array, weights, mode='valid')
window = 5
np.random.seed(1)
arr = np.random.randint(1, 100, size=30)
print("Original array (30 elements):")
print(arr)
ma = moving_average_convolve(arr, window)
print("Moving averages:")
print(ma.round(2))

#Question 18
rows = 4
cols = 4
matrix_4 = np.random.randint(1,50,size=(rows,cols))
print(f"Matrix - {matrix_4}")
matrix_4_inv = np.linalg.inv(matrix_4)
print(f"Inverse - {matrix_4_inv}")
identity_check = matrix_4 @ matrix_4_inv  #np.identity(4)
print(f"Identity Matrix  - {identity_check}")

# Check if result is identity matrix
is_identity = np.allclose(identity_check, np.eye(4))
print(f"\nIs identity matrix? {is_identity}")

#Question 19
rows = 6
cols = 6
np.random.seed(1)
matrix = np.random.randint(1,200,size=(rows,cols))
print(f"Matrix - {matrix}")
divisible_by_3 = matrix[matrix % 3 == 0]
print(f"After Divisible by 3- {divisible_by_3}")
#Approach 2
indices = np.where(matrix % 3 == 0)
rows, cols = indices
values = matrix[indices]

print("Detailed breakdown (using np.where):")
print(f"Row indices: {rows}")
print(f"Col indices: {cols}")
print(f"Values:      {values}")


#Question 20
# Two 1D arrays of different lengths
a = np.array([1, 2, 3, 4])      # Shape: (4,)
b = np.array([10, 20, 30])      # Shape: (3,)

print(f"Array a (shape {a.shape}): {a}")
print(f"Array b (shape {b.shape}): {b}")
print()

# Broadcasting for outer product
# a[:, np.newaxis] reshapes a to (4, 1)
# b remains (3,) which broadcasts to (4, 3)
outer_product = a[:, np.newaxis] * b

print("Outer product (4x3):")
print(outer_product)