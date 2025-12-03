#ORIGINAL

import pandas as pd
import matplotlib.pyplot as plt

# Load datasets
hours_df = pd.read_csv('/Users/sabiqadar/Downloads/annual-working-hours-per-worker/annual-working-hours-per-worker.csv')
divorce_df = pd.read_csv('/Users/sabiqadar/Downloads/divorces-per-1000-people/divorces-per-1000-people.csv')

# Filter for year 2018 and selected countries
countries = ['Japan', 'Sweden', 'Mexico', 'United Kingdom','United States']
filtered_hours = hours_df[(hours_df['Year'] == 2019) & (hours_df['Entity'].isin(countries))]
filtered_divorce = divorce_df[(divorce_df['Year'] == 2019) & (divorce_df['Entity'].isin(countries))]

# Merge datasets on Entity and Year
merged_df = pd.merge(filtered_hours, filtered_divorce, on=['Entity', 'Year'])

# Plotting
plt.figure(figsize=(8, 6))
plt.scatter(merged_df['Working hours per worker'], merged_df['Crude divorce rate'], color='red')

# Annotate each point with country name
for i, row in merged_df.iterrows():
    plt.text(row['Working hours per worker'] + 5, row['Crude divorce rate'], row['Entity'])

plt.title('Working Hours vs Divorce Rate (2019)')
plt.xlabel('Working Hours per Worker - annually')
plt.ylabel('Crude Divorce Rate')
plt.grid(True)
plt.tight_layout()
plt.show()

combined_df = pd.merge(hours_df, divorce_df, on=['Entity', 'Year'])
combined_df = combined_df[combined_df['Entity'].isin(countries)]

plt.figure(figsize=(10, 8))
bubble_sizes = (combined_df['Year'] - combined_df['Year'].min()) * 10  # Scale bubble size by year

scatter = plt.scatter(
    combined_df['Working hours per worker'],
    combined_df['Crude divorce rate'],
    s=bubble_sizes,
    c=combined_df['Year'],
    cmap='viridis',
    alpha=0.6
)

for i, row in combined_df.iterrows():
    plt.text(row['Working hours per worker'] + 5, row['Crude divorce rate'], row['Entity'])

plt.title('Working Hours vs Divorce Rate (Multiple Years)')
plt.xlabel('Working Hours per Worker - annually')
plt.ylabel('Crude Divorce Rate')
plt.colorbar(scatter, label='Year')
plt.grid(True)
plt.tight_layout()
plt.show()
