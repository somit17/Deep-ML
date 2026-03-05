import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsRegressor

# Data
X = np.array([8.0, 6.2, 7.2, 6.2]).reshape(-1, 1)
Y = np.array([160, 160, 168, 155])

# Train model
model = KNeighborsRegressor(n_neighbors=1)
model.fit(X, Y)

# Predict
barbie_rating = 7.4
barbie_duration = model.predict([[barbie_rating]])[0]

print(f"Barbie (rating {barbie_rating}) → {barbie_duration:.0f} minutes")

# Simple plot
plt.figure(figsize=(8, 5))
plt.scatter(X, Y, color='blue', s=100, label='Training Movies')
plt.scatter(barbie_rating, barbie_duration, color='red', s=200, marker='*', label='Barbie')
plt.xlabel('IMDB Rating')
plt.ylabel('Duration (minutes)')
plt.title(f'KNN: Barbie predicted = {barbie_duration:.0f} min')
plt.grid(True, alpha=0.3)
plt.legend()
plt.show()