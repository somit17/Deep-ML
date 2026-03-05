#Dataset
import numpy as np
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt

X = np.array([1, 2, 3, 4, 5, 6]).reshape(-1, 1)
Y = np.array([0, 0, 0, 1, 1, 1])

# Train logistic regression
model = LogisticRegression()
model.fit(X, Y)

# Get parameters
m = model.coef_[0][0]
c = model.intercept_[0]

print(f"Logistic Regression (scikit-learn):")
print(f"m = {m:.4f}")
print(f"c = {c:.4f}")
print(f"Probability for x=7: {model.predict_proba([[7]])[0][1]:.4f}")
print(f"Class prediction for x=7: {model.predict([[7]])[0]}")

# Plot
X_test = np.linspace(0, 8, 100).reshape(-1, 1)
Y_prob = model.predict_proba(X_test)[:, 1]

plt.figure(figsize=(10, 6))
plt.scatter(X, Y, color='red', s=100, label='Training data')
plt.plot(X_test, Y_prob, 'b-', linewidth=2, label='Logistic Regression')
plt.plot(7, model.predict_proba([[7]])[0][1], 'go', markersize=10, label='x=7 prediction')
plt.xlabel('X')
plt.ylabel('Probability')
plt.show()