import numpy as np
import matplotlib.pyplot as plt
from sklearn_extra.cluster import KMedoids

# --- 1. Prepare Data ---
S = ['D1','D2','D3','D4','D5','D6','D7','D8','D9','D10']
X = [2,5,8,3,7,6,1,4,9,5]
Y = [3,7,3,5,2,8,4,6,5,4]

# Combine X and Y into a matrix
data = np.array(list(zip(X, Y)))

# --- 2. Apply K-Medoids (k=2) ---
# random_state ensures you get the same result every time
model = KMedoids(n_clusters=2, method='pam', random_state=42)
model.fit(data)

# --- 3. Get Results ---
labels = model.labels_              # Which cluster each point belongs to
medoid_idx = model.medoid_indices_  # Indices of the actual medoid points
medoids = data[medoid_idx]          # Coordinates of the medoids

# --- 4. Print Output ---
print("=== K-Medoids Results (k=2) ===")
print(f"Medoid Coordinates: {medoids}")
print(f"Medoid Names: {[S[i] for i in medoid_idx]}")
print("\nCluster Assignments:")
for i, label in enumerate(labels):
    print(f"{S[i]} {list(data[i])} → Cluster {label}")

# --- 5. Plot ---
plt.figure(figsize=(8, 6))
colors = ['#FF6B6B', '#4ECDC4']  # Red for Cluster 0, Teal for Cluster 1

# Plot points
for i in range(2):
    cluster_points = data[labels == i]
    plt.scatter(cluster_points[:, 0], cluster_points[:, 1],
                c=colors[i], label=f'Cluster {i}', s=100, edgecolors='black')

# Plot Medoids (Stars)
plt.scatter(medoids[:, 0], medoids[:, 1],
            c='gold', s=200, marker='+', edgecolors='black',
            label='Medoids', zorder=5)

# Label points
for i, txt in enumerate(S):
    plt.annotate(txt, (data[i][0]+0.2, data[i][1]+0.2), fontsize=9)

plt.title("K-Medoids Clustering (k=2)")
plt.xlabel("X"); plt.ylabel("Y")
plt.legend(); plt.grid(alpha=0.3)
plt.show()