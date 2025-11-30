import numpy as np
import matplotlib.pyplot as plt

#generate synthetic data - monthly sales figures
def generated_data(n=12):
    x = np.arange(1, n+1)
    y = 20 * x + 180 + np.random.normal(0, 5, n)  # approx: y ≈ 20x + 180
    return x, y

#fit a line to the data using least squares
def line_of_fit(x, y):
    slope, intercept = np.polyfit(x, y, 1)
    return slope, intercept

#predict y values using the fitted line
def predicted_values(x, slope, intercept):
    return slope * x + intercept

#plot the data and the fitted line -  saves the plot as an image file
def plot_results(x, y, slope, intercept, save_path="plot.png"):
    y_pred = predicted_values(x, slope, intercept)
    plt.figure(figsize=(6, 4))
    plt.scatter(x, y, label="Sales Data")
    plt.plot(x, y_pred, label="Best Fit Line", linewidth=2)
    plt.xlabel("Month")
    plt.ylabel("Sales")
    plt.title("Monthly Sales with Best Fit Line")
    plt.legend()
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()

#main execution block for code
if __name__ == "__main__":
    x, y = generated_data()
    slope, intercept = line_of_fit(x, y)
    plot_results(x, y, slope, intercept)
    print(f"Slope: {slope:.2f}, Intercept: {intercept:.2f}")
