"""
boxplot.py

Loads the California Housing dataset (via scikit-learn) and generates a
boxplot of median income across all California census block groups.
The resulting figure is saved to figs/boxplot.png.
"""

import os
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing

# Create the required directories
os.makedirs('figs', exist_ok=True)

# Load California Housing dataset
housing = fetch_california_housing(as_frame=True)
df = housing.frame

# Generate a boxplot for median income (MedInc)
plt.figure(figsize=(8, 6))
df.boxplot(column=['MedInc'])
plt.title('Boxplot of Median Income in California')
plt.ylabel('Median Income (Tens of thousands of dollars)')

# Save the figure to the figs directory
output_path = 'figs/boxplot.png'
plt.savefig(output_path, dpi=150, bbox_inches='tight')
print(f"Figure successfully saved to {output_path}")

plt.show()
