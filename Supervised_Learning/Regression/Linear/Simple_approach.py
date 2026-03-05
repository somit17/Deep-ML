import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array([8, 10, 12]).reshape(-1, 1)
Y = np.array([10, 13, 16])

model = LinearRegression()
model.fit(X, Y)

print(f"Slope (m): {model.coef_[0]}")
print(f"Intercept (c): {model.intercept_}f")