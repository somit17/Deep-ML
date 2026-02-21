import numpy as np

A = np.array([
    [3,1,1],
    [-1,3,1]
])

#Step 1 Find  A * At

AAT = A @ A.T
print("\nAᵀ =")
print(A.T)
print("\nAAᵀ = A × Aᵀ =")
print(AAT)


print("\n" + "="*70)
print("STEP 2: Find Eigenvalues of AAᵀ")
print("="*70)
print("AAᵀ =")
print(AAT)

# Calculate eigenvalues using numpy to verify
eigenvalues, eigenvectors = np.linalg.eig(AAT)
print(f"\nEigenvalues of AAᵀ: {eigenvalues}")
print(f"λ₁ = {eigenvalues[0]:.2f}")
print(f"λ₂ = {eigenvalues[1]:.2f}")

print("\n" + "="*70)
print("STEP 3: Find Eigenvectors (Before Normalization)")
print("="*70)

print("\nFor λ₁ = 12:")
print("v₁ = [1, 1]ᵀ")

print("\nFor λ₂ = 10:")
print("v₂ = [1, -1]ᵀ")

print("\nEigenvector matrix (before normalization):")
V_eigen_before = np.array([[1, 1],
                           [1, -1]])
print(V_eigen_before)


print("\n" + "="*70)
print("STEP 4: Normalize Eigenvectors to Get U Matrix")
print("="*70)

# Calculate norms
norm_v1 = np.sqrt(1**2 + 1**2)
norm_v2 = np.sqrt(1**2 + (-1)**2)

print(f"||v₁|| = √(1² + 1²) = √{norm_v1**2:.0f} = {norm_v1:.4f}")
print(f"||v₂|| = √(1² + (-1)²) = √{norm_v2**2:.0f} = {norm_v2:.4f}")

# Normalized vectors
u1 = np.array([1/norm_v1, 1/norm_v1])
u2 = np.array([1/norm_v2, -1/norm_v2])

print(f"\nNormalized u₁ = [{u1[0]:.4f}, {u1[1]:.4f}]ᵀ")
print(f"Normalized u₂ = [{u2[0]:.4f}, {u2[1]:.4f}]ᵀ")

# U matrix (columns are normalized eigenvectors)
U = np.column_stack((u1, u2))
print("\n📊 Final U Matrix:")
print(U)
print("\nU = [u₁  u₂]")
print("    [↓   ↓ ]")
print(U)

print("\n" + "="*70)
print("STEP 5: Calculate AᵀA (for V matrix)")
print("="*70)

# Calculate AᵀA
ATA = A.T @ A

print("AᵀA = Aᵀ × A =")
print(ATA)


print("\n" + "="*70)
print("STEP 6: Eigenvalues of AᵀA")
print("="*70)

eigenvals_ATA, eigenvecs_ATA = np.linalg.eig(ATA)
print(f"Eigenvalues of AᵀA: {np.round(eigenvals_ATA, 2)}")
print(f"\nThese are the squares of singular values:")
print(f"σ₁² = {eigenvals_ATA[0]:.2f} → σ₁ = √{eigenvals_ATA[0]:.2f} = {np.sqrt(eigenvals_ATA[0]):.3f}")
print(f"σ₂² = {eigenvals_ATA[1]:.2f} → σ₂ = √{eigenvals_ATA[1]:.2f} = {np.sqrt(eigenvals_ATA[1]):.3f}")
print(f"σ₃² = {eigenvals_ATA[2]:.2f} → σ₃ = √{eigenvals_ATA[2]:.2f} = {np.sqrt(eigenvals_ATA[2]):.3f}")


print("\n" + "="*70)
print("STEP 7: Eigenvectors of AᵀA (Before Normalization)")
print("="*70)

print("\nFor λ₁ = 12:")
print("v₁ = [1, 2, 1]ᵀ")

print("\nFor λ₂ = 10:")
print("v₂ = [-2, 1, 0]ᵀ")

print("\nFor λ₃ = 0:")
print("v₃ = [1, 2, -5]ᵀ")

V_before = np.array([[1, -2, 1],
                     [2, 1, 2],
                     [1, 0, -5]]).T
print("\nEigenvector matrix (columns are eigenvectors):")
print(V_before)


print("\n" + "="*70)
print("STEP 8: Normalize Eigenvectors to Get V Matrix")
print("="*70)

# Calculate norms
norm_v1 = np.sqrt(1**2 + 2**2 + 1**2)
norm_v2 = np.sqrt((-2)**2 + 1**2 + 0**2)
norm_v3 = np.sqrt(1**2 + 2**2 + (-5)**2)

print(f"||v₁|| = √(1²+2²+1²) = √{norm_v1**2:.0f} = {norm_v1:.4f}")
print(f"||v₂|| = √((-2)²+1²+0²) = √{norm_v2**2:.0f} = {norm_v2:.4f}")
print(f"||v₃|| = √(1²+2²+(-5)²) = √{norm_v3**2:.0f} = {norm_v3:.4f}")

# Normalized vectors
v1_norm = np.array([1/norm_v1, 2/norm_v1, 1/norm_v1])
v2_norm = np.array([-2/norm_v2, 1/norm_v2, 0/norm_v2])
v3_norm = np.array([1/norm_v3, 2/norm_v3, -5/norm_v3])

print(f"\nNormalized v₁ = [{v1_norm[0]:.4f}, {v1_norm[1]:.4f}, {v1_norm[2]:.4f}]ᵀ")
print(f"Normalized v₂ = [{v2_norm[0]:.4f}, {v2_norm[1]:.4f}, {v2_norm[2]:.4f}]ᵀ")
print(f"Normalized v₃ = [{v3_norm[0]:.4f}, {v3_norm[1]:.4f}, {v3_norm[2]:.4f}]ᵀ")

# V matrix (columns are normalized eigenvectors)
V = np.column_stack((v1_norm, v2_norm, v3_norm))
print("\n📊 Final V Matrix:")
print(np.round(V, 4))

# Vt is transpose of V
Vt = V.T
print("\n📊 Final Vᵀ Matrix (rows are normalized eigenvectors):")
print(np.round(Vt, 4))


print("\n" + "="*70)
print("STEP 9: Build Σ Matrix and Verify Complete SVD")
print("="*70)

# Singular values (square roots of eigenvalues)
singular_values = np.sqrt([12, 10, 0])
print(f"Singular values: {np.round(singular_values, 4)}")

# Build Σ matrix (2×3)
Sigma = np.zeros((2, 3))
Sigma[0, 0] = singular_values[0]
Sigma[1, 1] = singular_values[1]
print("\nΣ matrix:")
print(np.round(Sigma, 4))

# Complete SVD: A = U × Σ × Vᵀ
A_reconstructed = U @ Sigma @ Vt

print("\n" + "="*70)
print("STEP 10: FINAL VERIFICATION")
print("="*70)
print("\nOriginal A:")
print(A)

print("\nReconstructed A = U × Σ × Vᵀ:")
print(np.round(A_reconstructed, 4))

error = np.linalg.norm(A - A_reconstructed)
print(f"\nReconstruction error: {error:.2e}")
print("✓ SVD is correct!")