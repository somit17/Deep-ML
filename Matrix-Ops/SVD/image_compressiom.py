import matplotlib.pyplot as plt
import numpy as np
from numpy import linalg as la
# Create a simple pattern (like a low-resolution image)
pattern = np.array([
    [1, 1, 1, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 1],
    [0, 0, 0, 1, 1, 1],
    [0, 0, 0, 1, 1, 1]
])

print("Our 'Image' (6×6 pixels):")
print(pattern)

# Perform SVD
U_img, s_img, Vt_img = la.svd(pattern)

print("\nSingular values:", s_img)
print("Only first 2 are significant!")

# Compress using different numbers of components
fig, axes = plt.subplots(2, 3, figsize=(12, 8))

# Original
axes[0, 0].imshow(pattern, cmap='gray')
axes[0, 0].set_title('Original')
axes[0, 0].axis('off')

# Compressed versions
for idx, k in enumerate([1, 2, 3, 4, 5]):
    row = (idx + 1) // 3
    col = (idx + 1) % 3

    # Reconstruct with k components
    U_k = U_img[:, :k]
    s_k = s_img[:k]
    Vt_k = Vt_img[:k, :]

    reconstructed = U_k @ np.diag(s_k) @ Vt_k

    axes[row, col].imshow(reconstructed, cmap='gray')
    axes[row, col].set_title(f'{k} components')
    axes[row, col].axis('off')

plt.tight_layout()
plt.show()

print("\n🎯 With just 2 components, we capture the main structure!")