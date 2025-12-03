import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chisquare
from model_forecasting import train_df, test_df, x_train, y_train, x_test, y_test


# Extract test data (observed values)
x_test = test_df['Ordinal'].values
y_test = test_df['Value'].values

# Range of polynomial degrees you want to test
degrees = range(1, 16)    
chi2_per_dof = []

for deg in degrees:
    # Fit polynomial to training data
    coeffs = np.polyfit(x_train, y_train, deg)
    model = np.poly1d(coeffs)

    # Predictions (expected values)
    expected = model(x_test)

    # If expected <= 0, fix it (needed for chi-square test)
    expected = np.where(expected <= 0, 1e-6, expected)

    # Compute chi-square statistic
    chi2_stat, p_val = chisquare(f_obs=y_test, f_exp=expected)

    # Degrees of freedom = (#test points) – (#params)
    dof = len(y_test) - (deg + 1)    # polynomial of degree n has n+1 params

    # Weighted χ² per degree of freedom
    chi2_dof = chi2_stat / dof
    chi2_per_dof.append(chi2_dof)


plt.figure(figsize=(12, 6))
plt.plot(degrees, chi2_per_dof, marker='o', linewidth=2)

plt.title("Model comparison by polynomial order", fontsize=16)
plt.xlabel("Polynomial order (n)", fontsize=14)
plt.ylabel("Weighted χ² per degree of freedom", fontsize=14)

plt.grid(True, linestyle='--', alpha=0.6)
plt.xticks(degrees)

plt.show()
