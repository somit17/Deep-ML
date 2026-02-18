import math

import numpy as np
from numpy.ma.core import diagonal

#Question 1
rows = 3
cols = 3
matrix_1 = np.random.randint(1,20,size=(rows,cols))
matrix_2 = np.random.randint(1,20,size=(rows,cols))
resultant_matrix = matrix_1 @ matrix_2
print(f"Matrix  multiplication  - {resultant_matrix}")
print(f"Determinant - {np.linalg.det(resultant_matrix)}")


#Question 2
rows = 10
cols = 10

arr  = np.random.rand(rows,cols)
bin_arr = np.where(arr > 0.5,1,0)
#Alternate
#binary_arr = (arr > 0.5).astype(int)
print(f"Binary = {bin_arr}")

#Question 3

def is_prime(n):
    if n < 2:
        return False
    for i in range(2,int(n ** 0.5)+1):
        if n % i == 0:
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