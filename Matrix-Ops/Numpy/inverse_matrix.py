import numpy as np

#Matrix Creation

matrix_2d = np.array([
    [7,2],
    [17,5]
])
print(f"Matrix 2D - {matrix_2d}")
print(f"Determinant - {np.linalg.det(matrix_2d)}")
print(f"Inverse of Matrix - {np.linalg.inv(matrix_2d)}")


matrix_3d = np.array([
    [5,3,7],
    [2,-5,8],
    [-6,4,9]
])
print(f"Matrix 3D - {matrix_3d}")
print(f"Determinant - {np.linalg.det(matrix_3d)}")
print(f"Inverse - {np.linalg.inv(matrix_3d)}")