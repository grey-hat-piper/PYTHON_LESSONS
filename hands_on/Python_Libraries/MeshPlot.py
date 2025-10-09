import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Use Seaborn to set the aesthetic style of the plot
# This is where Seaborn contributes, making the plot visually pleasing
sns.set_style("darkgrid") # Try "darkgrid" or "dark" for a different look!

# Create a function for the surface we want to plot
def three_d_surface(x, y):
    """Calculates the height Z based on X and Y coordinates."""
    return np.sin(np.sqrt(x**2 + y**2))

# Prepare the data: Create a grid of points
x_values = np.linspace(-6, 6, 40) # 40 points from -6 to 6
y_values = np.linspace(-6, 6, 40)
X, Y = np.meshgrid(x_values, y_values) # Weave the grid

# Calculate the height (Z) for every point on the grid
Z = three_d_surface(X, Y)

# Now, use Matplotlib to create the 3D plot on the styled canvas
fig = plt.figure(figsize=(10, 8))
# The key: create a 3D axes object
ax = fig.add_subplot(111, projection='3d')

# Plot the surface. Seaborn's style influences the look of this plot.
# 'cmap' defines the color map. 'viridis', 'plasma', 'coolwarm' are great options.
# 'alpha' controls transparency (0.0 to 1.0).
surface = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none', alpha=0.9)

# Add a color bar which maps values to colors, like a legend for height
fig.colorbar(surface, ax=ax, shrink=0.5, aspect=10, label='Height (Z)')

# Add labels to each axis
ax.set_xlabel('X Distance')
ax.set_ylabel('Y Distance')
ax.set_zlabel('Z Height')
ax.set_title('Topography of the Data: A 3D Surface Plot', fontsize=14)

# Let's adjust the viewing angle for a better perspective
ax.view_init(elev=20, azim=35) # Elevation and azimuth angles

plt.tight_layout()
plt.show()