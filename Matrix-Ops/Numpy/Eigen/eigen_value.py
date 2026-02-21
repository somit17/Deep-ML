import numpy as np
import numpy.linalg as la

# Step 1: Create the matrix
A = np.array([[4, 1],
              [2, 3]])

print("=" * 60)
print("EXAMPLE 1: Basic 2×2 Matrix")
print("=" * 60)
print("Matrix A:")
print(A)
print()

# Step 2: Calculate eigenvalues and eigenvectors
eigenvalues, eigenvectors = la.eig(A)

print("RESULTS:")
print("-" * 40)
print("Eigenvalues:")
for i, val in enumerate(eigenvalues):
    print(f"  λ{i + 1} = {val:.4f}")
print()

print("Eigenvectors (as columns):")
print(eigenvectors)
print()

# Step 3: Display eigenvectors individually
print("Individual Eigenvectors:")
for i in range(len(eigenvalues)):
    print(f"v{i + 1} = {eigenvectors[:, i]}")
print()

# Step 4: Verify the eigen equation A·v = λ·v
print("VERIFICATION:")
print("-" * 40)
for i in range(len(eigenvalues)):
    λ = eigenvalues[i]
    v = eigenvectors[:, i].reshape(-1, 1)

    # Left side: A·v
    left = A @ v

    # Right side: λ·v
    right = λ * v

    print(f"For λ = {λ:.4f}:")
    print(f"  A·v = {left.flatten()}")
    print(f"  λ·v = {right.flatten()}")
    print(f"  Difference: {la.norm(left - right):.2e}")
    print()


# Step 5: Detailed analysis
print("DETAILED ANALYSIS:")
print("-"*40)

# 5.1 Check if eigenvalues are correct using trace and determinant
trace_A = np.trace(A)
det_A = la.det(A)
sum_eigenvals = np.sum(eigenvalues)
prod_eigenvals = np.prod(eigenvalues)

print("Properties Check:")
print(f"  Trace(A) = {trace_A}")
print(f"  Sum of eigenvalues = {sum_eigenvals:.4f}")
print(f"  Determinant(A) = {det_A:.4f}")
print(f"  Product of eigenvalues = {prod_eigenvals:.4f}")
print()

# 5.2 Check orthogonality (for non-symmetric matrices, eigenvectors aren't necessarily orthogonal)
print("Eigenvector Relationships:")
for i in range(len(eigenvalues)):
    for j in range(i+1, len(eigenvalues)):
        dot_product = np.dot(eigenvectors[:, i], eigenvectors[:, j])
        print(f"  v{i+1}·v{j+1} = {dot_product:.4f}")
print()

# 5.3 Normalize and verify
print("Normalized Eigenvectors (they already are normalized by NumPy):")
for i in range(len(eigenvalues)):
    norm = la.norm(eigenvectors[:, i])
    print(f"  ||v{i+1}|| = {norm:.4f}")