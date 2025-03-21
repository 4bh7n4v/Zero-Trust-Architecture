import matplotlib.pyplot as plt
import numpy as np

# Data: 4 groups, each with 4 bars
groups = ['300', '600', '1500', '12000']
bar_labels = ['Without Micro-segmentation', 'Proposed Solution', 'Vmware NSX', 'Cisco ACI']  # Labels for the 4 bars in each group

# Values for each bar in each group (4 groups x 4 bars)
data = [
    [300, 312, 318, 315],  # 300
    [295, 307, 315, 310],  # 600
    [317, 330, 335, 331],  # 1500
    [361, 375, 380, 376]   # 12000
]

# Colors for each bar type (A, B, C, D)
colors = ['chocolate', 'darkseagreen', 'darkturquoise', 'crimson']

# Set figure size
plt.figure(figsize=(12, 6))

# Width of each bar and spacing between groups
bar_width = 0.15
group_spacing = 0.05  # Space between groups

# Calculate positions for each bar
x = np.arange(len(groups))  # Base positions for groups

# Plot bars for each type (A, B, C, D)
for i in range(len(bar_labels)):
    # Offset each bar within the group
    bar_positions = [pos + (bar_width + group_spacing) * i for pos in x]
    plt.bar(bar_positions, 
            [data[group][i] for group in range(len(groups))], 
            width=bar_width, 
            label=bar_labels[i], 
            color=colors[i])

# Customize the chart
plt.xlabel('Data (Bytes)', fontsize=12)
plt.ylabel('Jitter (micro seconds)', fontsize=12)
plt.title('Jitter measurement results from App to DB', fontsize=14)
plt.xticks([i + bar_width * 1.5 for i in x], groups)  # Center group labels
plt.legend(title='Bar Types')
plt.grid(True, linestyle='--', alpha=0.5)

# Add value labels on top of each bar
for i in range(len(bar_labels)):
    bar_positions = [pos + (bar_width + group_spacing) * i for pos in x]
    for j, pos in enumerate(bar_positions):
        plt.text(pos, data[j][i] + 1, str(data[j][i]), ha='center', va='bottom')

# Adjust layout
plt.tight_layout()

# Display the chart
plt.show()
