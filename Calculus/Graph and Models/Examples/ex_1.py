import numpy as np
import matplotlib.pyplot as plt

# Create x values (more points for smooth curve)
x = np.linspace(-2.5, 3.5, 200)
y = x**2 - 2

# Create the plot
plt.figure(figsize=(10, 6))

# Plot the smooth curve
plt.plot(x, y, 'b-', linewidth=2, label='y = x² - 2')

# Plot the points from the table
x_points = [-2, -1, 0, 1, 2, 3]
y_points = [2, -1, -2, -1, 2, 7]
plt.plot(x_points, y_points, 'ro', markersize=8, label='Table points')

# Add labels and title
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.title('Graph of y = x² - 2', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.legend()

# Add x and y axes lines
plt.axhline(y=0, color='k', linestyle='-', linewidth=0.5)
plt.axvline(x=0, color='k', linestyle='-', linewidth=0.5)

# Add some annotations
plt.text(2.5, 6, 'Parabola', fontsize=12, style='italic')
plt.text(0.5, -1.5, 'Vertex', fontsize=10, ha='center')

# Set axis limits for better view
plt.xlim(-2.5, 3.5)
plt.ylim(-3, 8)

plt.show()