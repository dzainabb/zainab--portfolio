#MULTIPLE COUNTIES WITH REGRESSION LINE

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read CSVs
x_data = pd.read_csv('/users/sabiqadar/Downloads/annual-working-hours-per-worker/annual-working-hours-per-worker.csv')
y_data = pd.read_csv('/users/sabiqadar/Downloads/divorces-per-1000-people/divorces-per-1000-people.csv')

# Parameters
countries = ['United Kingdom', 'United States', 'Mexico']
start_year = 2013
end_year = 2019

# Merge datasets on Entity and Year
merged = pd.merge(
    x_data[['Entity','Year','Working hours per worker']],
    y_data[['Entity','Year','Crude divorce rate']],
    on=['Entity','Year']
)

# Filter by countries and years
filtered = merged[(merged['Entity'].isin(countries)) & 
                  (merged['Year'] >= start_year) & 
                  (merged['Year'] <= end_year)]

# Scatter plot with regression lines
plt.figure(figsize=(10,6))
sns.lmplot(
    data=filtered,
    x='Working hours per worker',
    y='Crude divorce rate',
    hue='Entity',
    markers='o',
    height=6,
    aspect=1.5,
    ci=None
)

plt.xlabel('Average Hours Worked (Annually)')
plt.ylabel('Crude Divorce Rate')
plt.title(f'Working Hours vs Divorce Rate ({start_year}-{end_year})')
plt.grid(True)
plt.show()
