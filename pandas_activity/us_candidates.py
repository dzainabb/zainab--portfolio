import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
df = pd.read_csv('/Users/sabiqadar/Downloads/US-2016-primary.csv')

# Plot a histogram of a single column in the DataFrame
df.hist(column='fraction_votes')

# Set the title and axis labels
plt.title('Histogram of votes fraction')
plt.xlabel('Values')
plt.ylabel('Frequency')

# Display the histogram
plt.show()