import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Load data
data = pd.read_csv('graphs_for_presentation/all_data/divorces-per-1000-people.csv')

# Filter for United Kingdom
uk = data[data['Entity'] == 'United Kingdom']

# Define a quadratic model
def quadratic_model(x, a, b, c):
    return a * x**2 + b * x + c

# Fit the model
popt, pcov = curve_fit(quadratic_model, uk['Year'], uk['Crude divorce rate'])

# Extract parameters
a, b, c = popt

# Generate smooth curve for plotting
x_curve = np.linspace(uk['Year'].min(), uk['Year'].max(), 200)
y_curve = quadratic_model(x_curve, a, b, c)

# Plot
plt.scatter(uk['Year'], uk['Crude divorce rate'], color='teal', alpha=0.8, label='Data')
plt.plot(x_curve, y_curve, color='blue', label='Quadratic Fit')

# Display equation on chart
equation_text = f"y = {a:.5e}x² + {b:.3f}x + {c:.2f}"
plt.text(uk['Year'].min(), uk['Crude divorce rate'].max(), equation_text,
         fontsize=10, color='blue', ha='left', va='center')

# Labels and styling
plt.xlabel('Year')
plt.ylabel('Crude Divorce Rate (per 1000 people)')
plt.title('Divorce Rate Over Time - United Kingdom (Quadratic Fit)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
