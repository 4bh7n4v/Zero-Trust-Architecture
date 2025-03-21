import matplotlib.pyplot as plt
import numpy as np

# Data: 2 groups, each with 2 bars
groups = ['College', 'Hospital']
bar_labels = ['Flat', 'Seg']  # Labels for the 2 bars in each group

# Values for each bar in each group (2 groups x 2 bars)
data = [
    [1, 0.46],  # Group 1
    [1, 0.35]   # Group 2
]

# Colors for each bar type (X, Y)
colors = ['skyblue', 'lightcoral']

# Set figure size
plt.figure(figsize=(8, 5))

# Width of each bar
bar_width = 0.35

# Calculate positions for each bar
x = np.arange(len(groups))  # Base positions for groups

# Plot bars for each type (X, Y)
for i in range(len(bar_labels)):
    # Offset each bar within the group
    bar_positions = [pos + bar_width * i for pos in x]
    plt.bar(bar_positions, 
            [data[group][i] for group in range(len(groups))], 
            width=bar_width, 
            label=bar_labels[i], 
            color=colors[i])

# Customize the chart
# plt.xlabel('Groups', fontsize=12)
plt.ylabel('Average Closeness', fontsize=12)
plt.title('Average Closeness', fontsize=14)
plt.xticks([i + bar_width / 2 for i in x], groups)  # Center group labels
plt.legend(title='Bar Types')
plt.grid(True, linestyle='--', alpha=0.5)

# Add value labels on top of each bar
for i in range(len(bar_labels)):
    bar_positions = [pos + bar_width * i for pos in x]
    for j, pos in enumerate(bar_positions):
        plt.text(pos, data[j][i], str(data[j][i]), ha='center', va='bottom')

# Adjust layout
plt.tight_layout()

# Display the chart
plt.show()
