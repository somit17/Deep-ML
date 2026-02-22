import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate

# Dataset
X = np.array([2.5, 0.5, 2.2, 1.9, 3.1, 2.3, 2.0, 1.0, 1.5, 1.1])
Y = np.array([2.4, 0.7, 2.9, 2.2, 3.0, 2.7, 1.6, 1.1, 1.6, 0.9])
n = len(X)

print("=" * 80)
print("EXAMPLE 1: COMPLETE MANUAL PCA CALCULATIONS")
print("=" * 80)
print(f"Dataset: {n} points")
print("-" * 80)

# ============================================================================
# STEP 1: Calculate Means (Manual)
# ============================================================================
print("\n" + "=" * 80)
print("STEP 1: CALCULATE MEANS")
print("=" * 80)

# Manual mean calculation
sum_x = 0
sum_y = 0
for i in range(n):
    sum_x += X[i]
    sum_y += Y[i]
    print(f"  After adding point {i + 1}: X sum = {sum_x:.2f}, Y sum = {sum_y:.2f}")

mean_x = sum_x / n
mean_y = sum_y / n

print(f"\nMean X = {sum_x} / {n} = {mean_x:.4f} ≈ {mean_x:.2f}")
print(f"Mean Y = {sum_y} / {n} = {mean_y:.4f} ≈ {mean_y:.2f}")

# ============================================================================
# STEP 2: Calculate Deviations from Mean (Manual)
# ============================================================================
print("\n" + "=" * 80)
print("STEP 2: CALCULATE DEVIATIONS FROM MEAN")
print("=" * 80)

dev_x = []
dev_y = []

print("\nDeviations (X - mean_x) and (Y - mean_y):")
print("-" * 80)
print(f"{'Point':<6} {'X':<8} {'Y':<8} {'X-μx':<12} {'Y-μy':<12} {'Formula X-μx':<25} {'Formula Y-μy':<25}")
print("-" * 80)

for i in range(n):
    dx = X[i] - mean_x
    dy = Y[i] - mean_y
    dev_x.append(dx)
    dev_y.append(dy)
    print(
        f"{i + 1:<6} {X[i]:<8.2f} {Y[i]:<8.2f} {dx:<+12.4f} {dy:<+12.4f} {X[i]:.2f} - {mean_x:.2f} = {dx:+.4f} {Y[i]:.2f} - {mean_y:.2f} = {dy:+.4f}")

# Verify sum of deviations ≈ 0
print(f"\nSum of deviations X: {sum(dev_x):.10f} (should be 0)")
print(f"Sum of deviations Y: {sum(dev_y):.10f} (should be 0)")

# ============================================================================
# STEP 3: Calculate Covariance Matrix Components (Manual)
# ============================================================================
print("\n" + "=" * 80)
print("STEP 3: CALCULATE COVARIANCE MATRIX")
print("=" * 80)
print("\nFormula: Cov(X,Y) = Σ[(xᵢ - μx)(yᵢ - μy)] / (n-1)")

# Calculate products, squares, and sums
products_xy = []
squares_x = []
squares_y = []

print("\n" + "-" * 100)
print(f"{'i':<3} {'X-μx':<10} {'Y-μy':<10} {'(X-μx)(Y-μy)':<16} {'(X-μx)²':<14} {'(Y-μy)²':<14} {'Step-by-step':<30}")
print("-" * 100)

for i in range(n):
    prod = dev_x[i] * dev_y[i]
    sq_x = dev_x[i] ** 2
    sq_y = dev_y[i] ** 2

    products_xy.append(prod)
    squares_x.append(sq_x)
    squares_y.append(sq_y)

    print(f"{i + 1:<3} {dev_x[i]:<+10.4f} {dev_y[i]:<+10.4f} {prod:<+16.4f} {sq_x:<14.4f} {sq_y:<14.4f} "
          f"({dev_x[i]:+.2f})×({dev_y[i]:+.2f}) = {prod:+.2f}")

# Calculate sums
sum_xy = sum(products_xy)
sum_xx = sum(squares_x)
sum_yy = sum(squares_y)

print("-" * 100)
print(f"{'SUM':<3} {'':<10} {'':<10} {sum_xy:<+16.4f} {sum_xx:<14.4f} {sum_yy:<14.4f}")

# Calculate covariance components
print("\nCalculating each covariance component:")
print("-" * 40)

# Cov(X,X)
cov_xx = sum_xx / (n - 1)
print(f"Cov(X,X) = {sum_xx:.4f} / {n - 1} = {cov_xx:.4f}")

# Cov(Y,Y)
cov_yy = sum_yy / (n - 1)
print(f"Cov(Y,Y) = {sum_yy:.4f} / {n - 1} = {cov_yy:.4f}")

# Cov(X,Y)
cov_xy = sum_xy / (n - 1)
print(f"Cov(X,Y) = {sum_xy:.4f} / {n - 1} = {cov_xy:.4f}")

# Cov(Y,X)
cov_yx = cov_xy

cov_matrix = np.array([[cov_xx, cov_xy], [cov_yx, cov_yy]])
print(f"\nCovariance Matrix:")
print(f"[{cov_xx:.4f}  {cov_xy:.4f}]")
print(f"[{cov_yx:.4f}  {cov_yy:.4f}]")

# ============================================================================
# STEP 4: Calculate Eigenvalues (Manual)
# ============================================================================
print("\n" + "=" * 80)
print("STEP 4: CALCULATE EIGENVALUES")
print("=" * 80)
print("\nCharacteristic equation: det(A - λI) = 0")
print(f"For matrix A = [{cov_xx:.4f}  {cov_xy:.4f}; {cov_yx:.4f}  {cov_yy:.4f}]")

# For 2x2 matrix: λ² - (a+d)λ + (ad - bc) = 0
a, b, c, d = cov_xx, cov_xy, cov_yx, cov_yy

trace = a + d
det = a * d - b * c

print(f"\nTrace (a+d) = {a:.4f} + {d:.4f} = {trace:.4f}")
print(f"Determinant (ad - bc) = ({a:.4f}×{d:.4f}) - ({b:.4f}×{c:.4f}) = {a * d:.4f} - {b * c:.4f} = {det:.4f}")

print(f"\nCharacteristic equation: λ² - ({trace:.4f})λ + ({det:.4f}) = 0")

# Quadratic formula: λ = [trace ± √(trace² - 4det)] / 2
discriminant = trace ** 2 - 4 * det
print(f"\nDiscriminant = trace² - 4det = {trace:.4f}² - 4×{det:.4f} = {discriminant:.4f}")

sqrt_disc = np.sqrt(discriminant)
print(f"√(discriminant) = √{discriminant:.4f} = {sqrt_disc:.4f}")

lambda1 = (trace + sqrt_disc) / 2
lambda2 = (trace - sqrt_disc) / 2

print(f"\nλ₁ = ({trace:.4f} + {sqrt_disc:.4f})/2 = {lambda1:.4f}")
print(f"λ₂ = ({trace:.4f} - {sqrt_disc:.4f})/2 = {lambda2:.4f}")

# Sort eigenvalues
eigenvalues = np.array([lambda1, lambda2])
idx = eigenvalues.argsort()[::-1]
eigenvalues = eigenvalues[idx]
print(f"\nSorted eigenvalues: λ₁ = {eigenvalues[0]:.4f}, λ₂ = {eigenvalues[1]:.4f}")

# ============================================================================
# STEP 5: Calculate Eigenvectors (Manual)
# ============================================================================
print("\n" + "=" * 80)
print("STEP 5: CALCULATE EIGENVECTORS")
print("=" * 80)

eigenvectors = np.zeros((2, 2))

print(f"\nFor λ₁ = {eigenvalues[0]:.4f}:")
print("-" * 40)
print("Solve (A - λ₁I)v = 0:")
print(f"[{a:.4f} - {eigenvalues[0]:.4f}      {b:.4f}   ] [v₁] = [0]")
print(f"[{c:.4f}      {d:.4f} - {eigenvalues[0]:.4f}] [v₂]   [0]")

# First eigenvector
a11 = a - eigenvalues[0]
a12 = b
a21 = c
a22 = d - eigenvalues[0]

print(f"\nMatrix becomes:")
print(f"[{a11:.4f}  {a12:.4f}]")
print(f"[{a21:.4f}  {a22:.4f}]")

print("\nFrom first equation: a11·v₁ + a12·v₂ = 0")
print(f"{a11:.4f}·v₁ + {a12:.4f}·v₂ = 0")

# Let v₁ = 1, solve for v₂
v1_1 = 1.0
v2_1 = -(a11 * v1_1) / a12
print(f"Let v₁ = 1, then:")
print(f"{a11:.4f}×1 + {a12:.4f}·v₂ = 0")
print(f"{a12:.4f}·v₂ = {-a11:.4f}")
print(f"v₂ = {-a11:.4f} / {a12:.4f} = {v2_1:.4f}")

# Normalize
norm1 = np.sqrt(v1_1 ** 2 + v2_1 ** 2)
eigenvector1 = np.array([v1_1 / norm1, v2_1 / norm1])
print(f"\nEigenvector (unnormalized): [{v1_1:.4f}, {v2_1:.4f}]")
print(f"Norm = √({v1_1:.4f}² + {v2_1:.4f}²) = √{v1_1 ** 2 + v2_1 ** 2:.4f} = {norm1:.4f}")
print(f"Normalized eigenvector: [{eigenvector1[0]:.4f}, {eigenvector1[1]:.4f}]")

print(f"\nFor λ₂ = {eigenvalues[1]:.4f}:")
print("-" * 40)

# Second eigenvector
a11 = a - eigenvalues[1]
a12 = b
a21 = c
a22 = d - eigenvalues[1]

print(f"Matrix becomes:")
print(f"[{a11:.4f}  {a12:.4f}]")
print(f"[{a21:.4f}  {a22:.4f}]")

print("\nFrom first equation: a11·v₁ + a12·v₂ = 0")
print(f"{a11:.4f}·v₁ + {a12:.4f}·v₂ = 0")

v1_2 = 1.0
v2_2 = -(a11 * v1_2) / a12
print(f"Let v₁ = 1, then v₂ = {v2_2:.4f}")

norm2 = np.sqrt(v1_2 ** 2 + v2_2 ** 2)
eigenvector2 = np.array([v1_2 / norm2, v2_2 / norm2])
print(f"\nNormalized eigenvector: [{eigenvector2[0]:.4f}, {eigenvector2[1]:.4f}]")

eigenvectors = np.column_stack((eigenvector1, eigenvector2))

# ============================================================================
# STEP 6: Calculate Explained Variance
# ============================================================================
print("\n" + "=" * 80)
print("STEP 6: EXPLAINED VARIANCE")
print("=" * 80)

total_var = eigenvalues[0] + eigenvalues[1]
explained_ratio = eigenvalues / total_var
cumulative = np.cumsum(explained_ratio)

print(f"Total variance = {eigenvalues[0]:.4f} + {eigenvalues[1]:.4f} = {total_var:.4f}")
print(
    f"\nPC1 explains: {eigenvalues[0]:.4f}/{total_var:.4f} = {explained_ratio[0]:.4f} = {explained_ratio[0] * 100:.2f}%")
print(
    f"PC2 explains: {eigenvalues[1]:.4f}/{total_var:.4f} = {explained_ratio[1]:.4f} = {explained_ratio[1] * 100:.2f}%")
print(f"\nCumulative with PC1: {cumulative[0] * 100:.2f}%")
print(f"Cumulative with both: {cumulative[1] * 100:.2f}%")

# ============================================================================
# STEP 7: Center Data and Project (Manual)
# ============================================================================
print("\n" + "=" * 80)
print("STEP 7: PROJECT DATA ONTO PRINCIPAL COMPONENTS")
print("=" * 80)

# Center the data
centered_data = np.column_stack((dev_x, dev_y))

print("\nProjection formula: PC_score = centered_data · eigenvector")
print("\nCalculating PC scores for each point:")
print("-" * 100)
print(f"{'Point':<6} {'Original':<15} {'Centered':<20} {'PC1 Score':<15} {'PC2 Score':<15} {'PC1 Calculation':<30}")
print("-" * 100)

pca_scores = []
for i in range(n):
    pc1 = centered_data[i, 0] * eigenvectors[0, 0] + centered_data[i, 1] * eigenvectors[1, 0]
    pc2 = centered_data[i, 0] * eigenvectors[0, 1] + centered_data[i, 1] * eigenvectors[1, 1]
    pca_scores.append([pc1, pc2])

    calc = f"({centered_data[i, 0]:+.2f}×{eigenvectors[0, 0]:.2f}) + ({centered_data[i, 1]:+.2f}×{eigenvectors[1, 0]:.2f})"
    print(
        f"{i + 1:<6} ({X[i]:.2f},{Y[i]:.2f}){'':<3} ({centered_data[i, 0]:+.2f},{centered_data[i, 1]:+.2f}){'':<3} {pc1:<+15.4f} {pc2:<+15.4f} {calc}")

pca_scores = np.array(pca_scores)

# ============================================================================
# VISUALIZATION
# ============================================================================
print("\n" + "=" * 80)
print("VISUALIZATION")
print("=" * 80)

fig, axes = plt.subplots(2, 3, figsize=(18, 12))

# Plot 1: Original Data
axes[0, 0].scatter(X, Y, s=100, alpha=0.7, color='blue')
axes[0, 0].axhline(y=mean_y, color='red', linestyle='--', alpha=0.5, label=f'Mean Y={mean_y:.2f}')
axes[0, 0].axvline(x=mean_x, color='green', linestyle='--', alpha=0.5, label=f'Mean X={mean_x:.2f}')
axes[0, 0].scatter(mean_x, mean_y, color='purple', s=200, marker='*', label='Centroid')
for i, (x, y) in enumerate(zip(X, Y)):
    axes[0, 0].annotate(f'{i + 1}', (x, y), xytext=(5, 5), textcoords='offset points')
axes[0, 0].set_xlabel('X')
axes[0, 0].set_ylabel('Y')
axes[0, 0].set_title('Original Data with Means')
axes[0, 0].legend()
axes[0, 0].grid(True, alpha=0.3)
axes[0, 0].axis('equal')

# Plot 2: Deviations Visualization
axes[0, 1].scatter(dev_x, dev_y, s=100, alpha=0.7, color='blue')
axes[0, 1].axhline(y=0, color='red', linestyle='--', alpha=0.5)
axes[0, 1].axvline(x=0, color='green', linestyle='--', alpha=0.5)
for i, (dx, dy) in enumerate(zip(dev_x, dev_y)):
    axes[0, 1].annotate(f'{i + 1}', (dx, dy), xytext=(5, 5), textcoords='offset points')
    # Draw lines from original to centered
    axes[0, 1].plot([X[i] - mean_x, 0], [Y[i] - mean_y, 0], 'gray', alpha=0.3)
axes[0, 1].set_xlabel('Deviation X (X - μx)')
axes[0, 1].set_ylabel('Deviation Y (Y - μy)')
axes[0, 1].set_title('Centered Data (Deviations from Mean)')
axes[0, 1].grid(True, alpha=0.3)
axes[0, 1].axis('equal')

# Plot 3: Covariance Visualization
cov_matrix_display = np.array([[cov_xx, cov_xy], [cov_yx, cov_yy]])
im = axes[0, 2].imshow(cov_matrix_display, cmap='coolwarm', aspect='auto', vmin=0, vmax=2)
for i in range(2):
    for j in range(2):
        text = axes[0, 2].text(j, i, f'{cov_matrix_display[i, j]:.4f}',
                               ha="center", va="center", color="black", fontsize=12)
axes[0, 2].set_xticks([0, 1])
axes[0, 2].set_yticks([0, 1])
axes[0, 2].set_xticklabels(['X', 'Y'])
axes[0, 2].set_yticklabels(['X', 'Y'])
axes[0, 2].set_title('Covariance Matrix')
plt.colorbar(im, ax=axes[0, 2])

# Plot 4: Principal Components
axes[1, 0].scatter(dev_x, dev_y, s=100, alpha=0.7, color='blue', label='Centered Data')
scale = 3
for i in range(2):
    vec = eigenvectors[:, i] * np.sqrt(eigenvalues[i]) * scale
    axes[1, 0].arrow(0, 0, vec[0], vec[1],
                     head_width=0.15, head_length=0.15,
                     fc=f'C{i + 2}', ec=f'C{i + 2}', linewidth=2,
                     label=f'PC{i + 1} (λ={eigenvalues[i]:.2f})')
axes[1, 0].axhline(y=0, color='k', linestyle='-', alpha=0.2)
axes[1, 0].axvline(x=0, color='k', linestyle='-', alpha=0.2)
axes[1, 0].set_xlabel('Deviation X')
axes[1, 0].set_ylabel('Deviation Y')
axes[1, 0].set_title('Principal Components (Eigenvectors)')
axes[1, 0].legend()
axes[1, 0].grid(True, alpha=0.3)
axes[1, 0].axis('equal')

# Plot 5: PCA Transformed Data
axes[1, 1].scatter(pca_scores[:, 0], pca_scores[:, 1], s=100, alpha=0.7, color='blue')
axes[1, 1].axhline(y=0, color='k', linestyle='--', alpha=0.3)
axes[1, 1].axvline(x=0, color='k', linestyle='--', alpha=0.3)
for i, (pc1, pc2) in enumerate(pca_scores):
    axes[1, 1].annotate(f'{i + 1}', (pc1, pc2), xytext=(5, 5), textcoords='offset points')
axes[1, 1].set_xlabel('First Principal Component (PC1)')
axes[1, 1].set_ylabel('Second Principal Component (PC2)')
axes[1, 1].set_title(
    f'Data in PCA Space\nPC1 Var: {np.var(pca_scores[:, 0]):.4f}, PC2 Var: {np.var(pca_scores[:, 1]):.4f}')
axes[1, 1].grid(True, alpha=0.3)

# Plot 6: Explained Variance
axes[1, 2].bar(range(1, 3), explained_ratio, alpha=0.7, color=['blue', 'orange'])
axes[1, 2].plot(range(1, 3), cumulative, 'ro-', linewidth=2, label='Cumulative')
axes[1, 2].set_xlabel('Principal Component')
axes[1, 2].set_ylabel('Explained Variance Ratio')
axes[1, 2].set_title('Variance Explained')
axes[1, 2].set_xticks([1, 2])
axes[1, 2].set_ylim([0, 1.1])
for i, (er, cum) in enumerate(zip(explained_ratio, cumulative)):
    axes[1, 2].text(i + 1, er + 0.05, f'{er * 100:.1f}%', ha='center', fontsize=10)
    axes[1, 2].text(i + 1, cum - 0.1, f'Cum: {cum * 100:.1f}%', ha='center', fontsize=9, color='red')
axes[1, 2].grid(True, alpha=0.3)
axes[1, 2].legend()

plt.tight_layout()
plt.show()

# ============================================================================
# FINAL SUMMARY TABLE
# ============================================================================
print("\n" + "=" * 80)
print("FINAL RESULTS SUMMARY")
print("=" * 80)

print("\n1. MEANS:")
print(f"   μx = {mean_x:.4f}")
print(f"   μy = {mean_y:.4f}")

print("\n2. COVARIANCE MATRIX:")
print(f"   [[{cov_xx:.4f}, {cov_xy:.4f}],")
print(f"    [{cov_yx:.4f}, {cov_yy:.4f}]]")

print("\n3. EIGENVALUES (Variance explained):")
print(f"   λ₁ = {eigenvalues[0]:.4f} ({explained_ratio[0] * 100:.2f}%)")
print(f"   λ₂ = {eigenvalues[1]:.4f} ({explained_ratio[1] * 100:.2f}%)")

print("\n4. EIGENVECTORS (Principal Components):")
print(f"   PC1 = [{eigenvectors[0, 0]:.4f}, {eigenvectors[1, 0]:.4f}]")
print(f"   PC2 = [{eigenvectors[0, 1]:.4f}, {eigenvectors[1, 1]:.4f}]")

print("\n5. PCA TRANSFORMED DATA:")
print("-" * 60)
print(f"{'Point':<8} {'Original (X,Y)':<20} {'PC1 Score':<15} {'PC2 Score':<15}")
print("-" * 60)
for i in range(n):
    print(f"{i + 1:<8} ({X[i]:.2f}, {Y[i]:.2f}){'':<8} {pca_scores[i, 0]:<+15.4f} {pca_scores[i, 1]:<+15.4f}")

print("\n" + "=" * 80)
print("INTERPRETATION:")
print("=" * 80)
print(f"• PC1 explains {explained_ratio[0] * 100:.2f}% of the variance")
print(f"• PC2 explains only {explained_ratio[1] * 100:.2f}% of the variance")
print(f"• The data can be reduced to 1 dimension with only {100 - explained_ratio[0] * 100:.2f}% information loss")
print(f"• The principal component direction is approximately 45°, showing X and Y are highly correlated")
print("=" * 80)