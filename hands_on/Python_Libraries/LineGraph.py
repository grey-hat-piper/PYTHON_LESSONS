import matplotlib.pyplot as plt
import numpy as np

# Our data: X-axis represents time (e.g., years, months)
x = [0, 1, 2, 3, 4, 5]

# Convert the string data to proper numerical values.
# We replace 'k' with 'e3' which means *1000, and convert to float.
y1 = [float(val.replace('k', 'e3')) for val in ['1000', '13k', '26k', '42k', '60k', '81k']]
y2 = [float(val.replace('k', 'e3')) for val in ['1000', '13k', '27k', '43k', '63k', '85k']]
#y3 = [float(val.replace('k', 'e3')) for val in ['1200', '15k', '30k', '45k', '65k', '90k']]


# Create a new figure, like preparing a fresh canvas
plt.figure(figsize=(10, 6)) # width, height in inches

# Plot the first data series with a solid line
plt.plot(x, y1, label='Production Line A', linestyle='-', marker='o')
# Plot the second data series with a dash-dot line
plt.plot(x, y2, label='Production Line B', linestyle='-.', marker='s')
# Plot the third data series with a dashed line
#plt.plot(x, y3, label='Production Line C', linestyle='-', marker='b')

# Add titles and labels to give context to our story
plt.xlabel("Season", fontsize=12)
plt.ylabel("Harvest Yield", fontsize=12)
plt.title('Village Harvest Over Time: The Story of Two Fields', fontsize=14)

# Add a legend to distinguish our lines
plt.legend()

# Add grid lines for easier reading, like guides on a map
plt.grid(True, linestyle='--', alpha=0.7)

# Display the final plot
plt.tight_layout() # Ensures everything fits nicely
plt.show()