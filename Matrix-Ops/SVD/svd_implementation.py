import numpy as np
from numpy import linalg as la

# ============================================================================
# STEP 1: Create a Simple Matrix
# ============================================================================
print("=" * 70)
print("🔷 STEP 1: CREATE A SIMPLE 2×2 MATRIX")
print("=" * 70)

# Let's use a matrix with nice round numbers
A = np.array([[3, 1],
              [1, 3]])

print("Our matrix A:")
print(A)
print("\n📌 This is a symmetric matrix (A = Aᵀ)")
print("   It represents data where both features are related")
print("   Shape: 2 rows × 2 columns")

# ============================================================================
# STEP 2: Perform SVD
# ============================================================================
print("\n" + "=" * 70)
print("🔷 STEP 2: PERFORM SVD")
print("=" * 70)

U, s, Vt = la.svd(A, full_matrices=True)

print("\n📦 SVD gives us 3 matrices:")
print("\n1️⃣ U matrix (Left Singular Vectors):")
print(U)
print("   Shape:", U.shape)
print("   → Shows the orientation of our data in row-space")

print("\n2️⃣ s vector (Singular Values):")
print(s)
print("   Shape:", s.shape)
print("   → Numbers showing how important each pattern is")

print("\n3️⃣ Vt matrix (Right Singular Vectors):")
print(Vt)
print("   Shape:", Vt.shape)
print("   → Shows the patterns in our column-space")

# ============================================================================
# STEP 3: Understanding the Singular Values
# ============================================================================
print("\n" + "=" * 70)
print("🔷 STEP 3: UNDERSTANDING SINGULAR VALUES (IMPORTANCE)")
print("=" * 70)

print(f"Singular values: {s[0]:.2f} and {s[1]:.2f}")

# Calculate importance percentages
total_importance = np.sum(s)
importance_pct1 = (s[0] / total_importance) * 100
importance_pct2 = (s[1] / total_importance) * 100

print(f"\n📊 IMPORTANCE BREAKDOWN:")
print(f"   • First pattern: {s[0]:.2f} ({importance_pct1:.1f}% of total)")
print(f"   • Second pattern: {s[1]:.2f} ({importance_pct2:.1f}% of total)")

print(f"\n✨ Key insight: Both patterns are equally important!")
print(f"   This makes sense because our matrix is symmetric and balanced.")

# ============================================================================
# STEP 4: Build the Sigma Matrix
# ============================================================================
print("\n" + "=" * 70)
print("🔷 STEP 4: BUILD SIGMA MATRIX (Σ)")
print("=" * 70)

# Create a zero matrix of correct size
Sigma = np.zeros((A.shape[0], A.shape[1]))
print("Step 4.1: Create empty matrix of correct shape")
print("np.zeros((2, 2)) =")
print(Sigma)

# Put singular values on diagonal
Sigma[:len(s), :len(s)] = np.diag(s)
print("\nStep 4.2: Put singular values on diagonal")
print("np.diag(s) creates:")
print(np.diag(s))
print("\nFinal Sigma matrix (Σ):")
print(Sigma)
print("\n📌 Sigma is a diagonal matrix with singular values")
print("   All off-diagonal elements are zero")

# ============================================================================
# STEP 5: Verify the SVD Equation A = U × Σ × Vᵀ
# ============================================================================
print("\n" + "=" * 70)
print("🔷 STEP 5: VERIFY A = U × Σ × Vᵀ")
print("=" * 70)

# Calculate U × Σ
U_Sigma = U @ Sigma
print("Step 5.1: First multiply U × Σ")
print("U × Σ =")
print(np.round(U_Sigma, 3))

# Complete the multiplication
A_reconstructed = U_Sigma @ Vt
print("\nStep 5.2: Then multiply (U × Σ) × Vᵀ")
print("U × Σ × Vᵀ =")
print(np.round(A_reconstructed, 3))

print("\nOriginal A:")
print(A)

# Check if reconstruction is perfect
error = la.norm(A - A_reconstructed)
print(f"\nReconstruction error: {error:.2e}")
print(f"✓ Perfect reconstruction! (error is practically zero)")

# ============================================================================
# STEP 6: Understanding What U and V Mean
# ============================================================================
print("\n" + "=" * 70)
print("🔷 STEP 6: UNDERSTANDING U AND V MATRICES")
print("=" * 70)

print("U matrix (shows patterns in rows):")
print(U)
print("\nEach column of U is a 'left singular vector'")
print("Column 1 = [0.71, 0.71]ᵀ → Both rows contribute equally")
print("Column 2 = [0.71, -0.71]ᵀ → Rows contribute oppositely")

print("\n" + "-" * 40)
print("Vt matrix (shows patterns in columns):")
print(Vt)
print("\nEach row of Vt is a 'right singular vector'")
print("Row 1 = [0.71, 0.71] → Both columns have same sign")
print("Row 2 = [0.71, -0.71] → Columns have opposite signs")

# ============================================================================
# STEP 7: See How SVD Reveals Matrix Structure
# ============================================================================
print("\n" + "=" * 70)
print("🔷 STEP 7: WHAT SVD TELLS US ABOUT OUR DATA")
print("=" * 70)

print("Our original matrix A:")
print(A)
print("\n🔍 SVD reveals that this matrix is made of two patterns:")

# Pattern 1 contribution
pattern1 = s[0] * np.outer(U[:, 0], Vt[0, :])
print(f"\nPattern 1 (importance: {s[0]:.2f}):")
print(np.round(pattern1, 2))
print("   → This pattern captures the 'average' behavior")

# Pattern 2 contribution
pattern2 = s[1] * np.outer(U[:, 1], Vt[1, :])
print(f"\nPattern 2 (importance: {s[1]:.2f}):")
print(np.round(pattern2, 2))
print("   → This pattern captures the 'difference' behavior")

# Sum of patterns
print("\nSum of both patterns (reconstructs original):")
print(np.round(pattern1 + pattern2, 2))

# ============================================================================
# STEP 8: Try Approximating with Less Information
# ============================================================================
print("\n" + "=" * 70)
print("🔷 STEP 8: APPROXIMATION WITH LESS INFORMATION")
print("=" * 70)

# Use only the first (most important) pattern
k = 1  # keep only first singular value
U_approx = U[:, :k]
s_approx = s[:k]
Vt_approx = Vt[:k, :]
Sigma_approx = np.diag(s_approx)

A_approx = U_approx @ Sigma_approx @ Vt_approx

print(f"Using only {k} most important pattern(s):")
print("Approximated matrix:")
print(np.round(A_approx, 2))

print("\nOriginal matrix:")
print(A)

approximation_error = la.norm(A - A_approx)
print(f"\nApproximation error: {approximation_error:.4f}")
print(f"We lost {(importance_pct2):.1f}% of the information!")

# ============================================================================
# STEP 9: Check Special Properties
# ============================================================================
print("\n" + "=" * 70)
print("🔷 STEP 9: SPECIAL PROPERTIES OF SVD")
print("=" * 70)

# 1. U is orthogonal: Uᵀ × U = I
print("1️⃣ U is orthogonal (Uᵀ × U = I):")
U_transpose_times_U = U.T @ U
print(np.round(U_transpose_times_U, 2))
print("   ✓ This is identity matrix!")

# 2. V is orthogonal: Vᵀ × V = I
print("\n2️⃣ V is orthogonal (Vᵀ × V = I):")
V = Vt.T  # Remember Vt is transpose of V
V_transpose_times_V = V.T @ V
print(np.round(V_transpose_times_V, 2))
print("   ✓ This is identity matrix!")

# 3. Relationship with eigenvalues (for square matrices)
print("\n3️⃣ Relationship with eigenvalues:")
eigenvals = la.eigvals(A)
print(f"   Eigenvalues of A: {eigenvals}")
print(f"   Singular values: {s}")
print(f"   For symmetric positive matrices, singular values = |eigenvalues|")
print(f"   ✓ True! |{eigenvals[0]:.2f}| = {s[0]:.2f}, |{eigenvals[1]:.2f}| = {s[1]:.2f}")

# ============================================================================
# STEP 10: Visual Summary
# ============================================================================
print("\n" + "=" * 70)
print("🔷 STEP 10: VISUAL SUMMARY")
print("=" * 70)

print("""
    SVD DECOMPOSITION VISUALIZED:

    Original Matrix          Left Vectors    Importance    Right Vectors
    ┌───────┐               ┌───────┐       ┌───────┐      ┌───────┐
    │ 3   1 │               │ 0.71  0.71 │   │ 4   0 │      │ 0.71  0.71 │
    │ 1   3 │       =       │ 0.71 -0.71 │   │ 0   2 │      │ 0.71 -0.71 │
    └───────┘               └───────┘       └───────┘      └───────┘
         A                       U               Σ              Vᵀ

    MEANING:
    • U shows: First column = both rows move together
              Second column = rows move opposite
    • Σ shows: First pattern is 2x stronger than second
    • Vᵀ shows: First pattern = both columns together
               Second pattern = columns opposite
""")




