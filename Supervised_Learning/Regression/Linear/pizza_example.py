#DataSet
import numpy as np
import matplotlib.pyplot as plt


X  = [8,10,12] #Diameter in inches
Y  =  [10,13,16] #Prices - Dependent

#Fomulae - y = mx+ c

mean_x = np.mean(X)
print(f"Mean X {mean_x}")
mean_y = np.mean(Y)
print(f"Mean Y {mean_y}")

#Standard deviations of X and Y
std_x = np.std(X)
std_y = np.std(Y)

# Calculate the slope (m) and intercept (c) using the least squares method
# m = Σ((x - x̄)(y - ȳ)) / Σ((x - x̄)²)

# Calculate deviations from means
deviations_x = [x - mean_x for x in X]
deviations_y = [y - mean_y for y in Y]
print(f"\nDeviations from mean X: {deviations_x}")
print(f"Deviations from mean Y: {deviations_y}")

# Product of deviations (for numerator)
product_deviations = [dx * dy for dx, dy in zip(deviations_x, deviations_y)]
print(f"Product of deviations: {product_deviations}")

# Sum of products (numerator)
sum_products = np.sum(product_deviations)
print(f"Sum of products (numerator): {sum_products}")

# Square of deviations of X (for denominator)
squared_deviations_x = [dx ** 2 for dx in deviations_x]
print(f"Squared deviations of X: {squared_deviations_x}")

# Sum of squared deviations (denominator)
sum_squared_deviations_x = np.sum(squared_deviations_x)
print(f"Sum of squared deviations (denominator): {sum_squared_deviations_x}")

# Calculate m = Slope
m = sum_products / sum_squared_deviations_x
print(f"\nSlope (m): {m}")

# Calculate c = Intercept (c = ȳ - m * x̄)
c = mean_y - m * mean_x
print(f"Intercept (c): {c}")

# ============ GENERATE GRAPH HERE ============
# Create the plot
plt.figure(figsize=(10, 6))

# Plot the original data points
plt.scatter(X, Y, color='red', marker='o', s=100, label='Actual Data Points', zorder=5)

# Generate points for the regression line
X_line = np.linspace(min(X)-1, max(X)+2, 100)
Y_line = m * X_line + c

# Make predictions
def predict(diameter):
    return m * diameter + c

# Plot the regression line
plt.plot(X_line, Y_line, color='blue', linewidth=2, label=f'Regression Line: y = {m:.2f}x + {c:.2f}')

# Add predicted point for 14 inches
plt.scatter(14, predict(14), color='green', marker='*', s=200,
           label=f'Predicted (14", ${predict(14):.2f})', zorder=6)

# Add labels and title
plt.xlabel('Diameter (inches)', fontsize=12)
plt.ylabel('Price ($)', fontsize=12)
plt.title('Linear Regression: Pizza Diameter vs Price', fontsize=14, fontweight='bold')
plt.show()
