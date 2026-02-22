import numpy as np
import matplotlib.pyplot as plt

# Dataset
X = np.array([2.5, 0.5, 2.2, 1.9, 3.1, 2.3, 2.0, 1.0, 1.5, 1.1])
Y = np.array([2.4, 0.7, 2.9, 2.2, 3.0, 2.7, 1.6, 1.1, 1.6, 0.9])

#Data --->
data = np.column_stack((X,Y))

#Get Mean
mean = np.mean(data, axis=0)

data_centered = data-mean



# STEP 2: Calculate covariance matrix
cov_matrix = np.cov(data_centered.T)

# STEP 3: Calculate eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)

# Sort by eigenvalue in descending order
idx = eigenvalues.argsort()[::-1]
eigenvalues = eigenvalues[idx]
eigenvectors = eigenvectors[:, idx]


# STEP 4: Calculate explained variance ratio
total_var = np.sum(eigenvalues)
explained_ratio = eigenvalues / total_var
cumulative_ratio = np.cumsum(explained_ratio)

for i, (ev, er) in enumerate(zip(eigenvalues, explained_ratio)):
    print(f"PC{i+1}: {ev:.4f} variance, {er*100:.2f}% explained")

print(f"\nCumulative with PC1: {cumulative_ratio[0]*100:.2f}%")
print(f"Cumulative with PC1+PC2: {cumulative_ratio[1]*100:.2f}%")


# STEP 5: Project data onto principal components
pca_scores = data_centered @ eigenvectors
print(f"Mean of PC1: {np.mean(pca_scores[:,0]):.10f} (should be 0)")
print(f"Mean of PC2: {np.mean(pca_scores[:,1]):.10f} (should be 0)")
print(f"Variance of PC1: {np.var(pca_scores[:,0]):.4f} (should equal λ₁={eigenvalues[0]:.4f})")
print(f"Variance of PC2: {np.var(pca_scores[:,1]):.4f} (should equal λ₂={eigenvalues[1]:.4f})")


# STEP 6: Reconstruction with reduced dimensions
# Keep only first principal component
pca_scores_k1 = pca_scores[:, 0].reshape(-1, 1)
data_reconstructed = (pca_scores_k1 @ eigenvectors[:, 0].reshape(1, -1)) + mean

print("Original vs Reconstructed (using only PC1):")
print("-"*60)
print(f"{'Original':<25} {'Reconstructed':<25} {'Error':<15}")
print("-"*60)
for i in range(len(X)):
    error = np.linalg.norm(data[i] - data_reconstructed[i])
    print(f"({data[i,0]:.2f}, {data[i,1]:.2f}){'':<10} ({data_reconstructed[i,0]:.2f}, {data_reconstructed[i,1]:.2f}){'':<10} {error:.4f}")

# ============================================================================
# Visualization
# ============================================================================
fig, axes = plt.subplots(2, 2, figsize=(15, 12))

# Plot 1: Original data with eigenvectors
axes[0,0].scatter(data[:,0], data[:,1], s=100, alpha=0.7, label='Original Data')
axes[0,0].scatter(mean[0], mean[1], color='red', s=200, marker='*', label='Mean')
for i in range(2):
    vec = eigenvectors[:, i] * np.sqrt(eigenvalues[i]) * 2
    axes[0,0].arrow(mean[0], mean[1], vec[0], vec[1],
                   head_width=0.1, head_length=0.1,
                   fc=f'C{i+1}', ec=f'C{i+1}', linewidth=2,
                   label=f'PC{i+1}')
axes[0,0].set_xlabel('X')
axes[0,0].set_ylabel('Y')
axes[0,0].set_title('Original Data with Principal Components')
axes[0,0].legend()
axes[0,0].grid(True, alpha=0.3)
axes[0,0].axis('equal')

# Plot 2: PCA transformed data
axes[0,1].scatter(pca_scores[:,0], pca_scores[:,1], s=100, alpha=0.7)
axes[0,1].axhline(y=0, color='k', linestyle='--', alpha=0.3)
axes[0,1].axvline(x=0, color='k', linestyle='--', alpha=0.3)
axes[0,1].set_xlabel('PC1')
axes[0,1].set_ylabel('PC2')
axes[0,1].set_title('Data in PCA Space')
axes[0,1].grid(True, alpha=0.3)

# Plot 3: Explained variance
axes[1,0].bar(range(1,3), explained_ratio, alpha=0.7, color=['blue', 'orange'])
axes[1,0].plot(range(1,3), cumulative_ratio, 'ro-', linewidth=2, label='Cumulative')
axes[1,0].set_xlabel('Principal Component')
axes[1,0].set_ylabel('Explained Variance Ratio')
axes[1,0].set_title('Explained Variance')
axes[1,0].set_xticks([1,2])
axes[1,0].set_ylim([0, 1.1])
for i, (er, cum) in enumerate(zip(explained_ratio, cumulative_ratio)):
    axes[1,0].text(i+1, er+0.05, f'{er*100:.1f}%', ha='center')
    axes[1,0].text(i+1, cum-0.1, f'Cum: {cum*100:.1f}%', ha='center', color='red')
axes[1,0].grid(True, alpha=0.3)
axes[1,0].legend()

# Plot 4: Reconstruction comparison
axes[1,1].scatter(data[:,0], data[:,1], s=100, alpha=0.7, label='Original')
axes[1,1].scatter(data_reconstructed[:,0], data_reconstructed[:,1],
                 s=100, alpha=0.7, label='Reconstructed (PC1 only)')
for i in range(len(X)):
    axes[1,1].plot([data[i,0], data_reconstructed[i,0]],
                  [data[i,1], data_reconstructed[i,1]],
                  'k--', alpha=0.3)
axes[1,1].set_xlabel('X')
axes[1,1].set_ylabel('Y')
axes[1,1].set_title('Original vs Reconstruction (PC1 only)')
axes[1,1].legend()
axes[1,1].grid(True, alpha=0.3)
axes[1,1].axis('equal')

plt.tight_layout()
plt.show()
