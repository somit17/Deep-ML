import numpy as np
import matplotlib.pyplot as plt

# Define the function
def f(x):
    return x**3 - 4*x

# Find intercepts analytically (as done in the textbook)
print("=" * 60)
print("EXAMPLE 2: Finding x- and y-intercepts of y = x³ - 4x")
print("=" * 60)

# Find x-intercepts (y = 0)
print("\n📐 FINDING x-INTERCEPTS (let y = 0):")
print("-" * 40)
print("x³ - 4x = 0")
print("x(x² - 4) = 0")
print("x(x - 2)(x + 2) = 0")
print("\nSolutions:")
print("  • x = 0")
print("  • x = 2")
print("  • x = -2")
print("\nx-intercepts: (0, 0), (2, 0), (-2, 0)")

# Find y-intercept (x = 0)
print("\n📐 FINDING y-INTERCEPT (let x = 0):")
print("-" * 40)
print("y = 0³ - 4(0) = 0")
print("y-intercept: (0, 0)")

# Create the plot
plt.figure(figsize=(12, 8))

# Generate x values for smooth curve
x = np.linspace(-3, 3, 400)
y = f(x)

# Plot the function
plt.plot(x, y, 'b-', linewidth=2, label='y = x³ - 4x')

# Mark the intercepts
x_intercepts = [-2, 0, 2]
y_intercepts = [0, 0, 0]
plt.scatter(x_intercepts, y_intercepts, color='red', s=100, zorder=5,
           label='Intercepts', edgecolors='black', linewidth=2)

# Label the intercepts
for x_int, y_int in zip(x_intercepts, y_intercepts):
    plt.annotate(f'({x_int}, {y_int})', (x_int, y_int),
                xytext=(10, 10 if x_int != 0 else -20),
                textcoords='offset points', fontsize=11,
                bbox=dict(boxstyle="round,pad=0.3", facecolor="yellow", alpha=0.7))

# Add grid and axes
plt.grid(True, alpha=0.3)
plt.axhline(y=0, color='k', linestyle='-', linewidth=1)
plt.axvline(x=0, color='k', linestyle='-', linewidth=1)

# Labels and title
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.title('Figure P.6: Graph of y = x³ - 4x', fontsize=14, fontweight='bold')
plt.legend(loc='upper left')

# Set axis limits
plt.xlim(-3, 3)
plt.ylim(-6, 6)

plt.tight_layout()
plt.show()