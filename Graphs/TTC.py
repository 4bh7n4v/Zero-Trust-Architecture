import matplotlib.pyplot as plt
import numpy as np

# Data: 4 groups, each with 3 bars
groups = ['Control Flat Network', 'Use case 1', 'Use case 2', 'Use case 3']
bar_labels = ['100 workloads', '200 workloads', '1000 workloads']  # Labels for the 3 bars in each group

# Values for each bar in each group (4 groups x 3 bars)
data = [
    [1, 1.5, 2.5],  # Group 1
    [2, 4, 7.5],  # Group 2
    [3, 4.5, 11],  # Group 3
    [5, 9, 24]   # Group 4
]

# Colors for each bar type (X, Y, Z)
colors = ['skyblue', 'lightcoral', 'lightgreen']

# Set figure size
plt.figure(figsize=(10, 6))  # Slightly wider to accommodate 4 groups

# Width of each bar
bar_width = 0.25  # Adjusted for 3 bars per group

# Calculate positions for each bar
x = np.arange(len(groups))  # Base positions for groups

# Plot bars for each type (X, Y, Z)
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
plt.ylabel('Hours', fontsize=12)
plt.title('Time To Completion In Hours', fontsize=14)
plt.xticks([i + bar_width for i in x], groups)  # Center group labels
plt.legend(title='Bar Types')
plt.grid(True, linestyle='--', alpha=0.5)

# Add value labels immediately above each bar
for i in range(len(bar_labels)):
    bar_positions = [pos + bar_width * i for pos in x]
    for j, pos in enumerate(bar_positions):
        plt.text(pos, data[j][i] + 0.25, str(data[j][i]), ha='center', va='bottom')

# Adjust layout
plt.tight_layout()

# Display the chart
plt.show()
