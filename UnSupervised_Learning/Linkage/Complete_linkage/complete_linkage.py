import numpy as np
import pandas as pd
from scipy.spatial.distance import pdist, squareform
from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt

# Data
S = ['S1','S2','S3','S4','S5','S6']
X = [4,1,2,3,6,5]
Y = [3,4,1,8,9,1]
data = np.array(list(zip(X, Y)))

# Distance matrix
dist_matrix = squareform(pdist(data, metric='euclidean'))
print("Distance Matrix:\n", pd.DataFrame(dist_matrix, index=S, columns=S).round(3))


# Complete Linkage Clustering
Z_complete = linkage(data, method='complete')
# Plot dendrogram
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
dendrogram(Z_complete, labels=S, color_threshold=5.0)
plt.axhline(y=5.0, color='red', linestyle='--', label='Cut at 5.0')
plt.title("Complete Linkage Dendrogram")
plt.xlabel("Sample")
plt.ylabel("Euclidean Distance")
plt.legend()
plt.grid(axis='y', alpha=0.3)
plt.show()