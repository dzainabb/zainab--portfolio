#different from the previous one as it includes multiple years in one graph - and more than 2 counties

import pandas as pd
import matplotlib.pyplot as plt

# Load datasets
hours_df = pd.read_csv('/Users/sabiqadar/Downloads/annual-working-hours-per-worker/annual-working-hours-per-worker.csv')
divorce_df = pd.read_csv('/Users/sabiqadar/Downloads/divorces-per-1000-people/divorces-per-1000-people.csv')

# Define countries and years
countries = ['Japan', 'Sweden', 'Mexico', 'United Kingdom', 'United States']
years = [2015, 2019]
colors = {2015: 'red', 2019: 'blue'}

# Country name to ISO code mapping
country_codes = {
    'Japan': 'JPN',
    'Sweden': 'SWE',
    'Mexico': 'MEX',
    'United Kingdom': 'GBR',
    'United States': 'USA'
}

plt.figure(figsize=(10, 7))

# Loop through years and plot each set
for year in years:
    filtered_hours = hours_df[(hours_df['Year'] == year) & (hours_df['Entity'].isin(countries))]
    filtered_divorce = divorce_df[(divorce_df['Year'] == year) & (divorce_df['Entity'].isin(countries))]
    merged_df = pd.merge(filtered_hours, filtered_divorce, on=['Entity', 'Year'])

    plt.scatter(
        merged_df['Working hours per worker'],
        merged_df['Crude divorce rate'],
        color=colors[year],
        label=str(year)
    )

    # Annotate each point with country code
    for i, row in merged_df.iterrows():
        code = country_codes.get(row['Entity'], row['Entity'])  # fallback to name if code missing
        plt.text(row['Working hours per worker'] + 5, row['Crude divorce rate'], code, fontsize=9)

# Final touches
plt.title('Working Hours vs Divorce Rate (Multiple Years)')
plt.xlabel('Working Hours per Worker - annually')
plt.ylabel('Crude Divorce Rate')
plt.grid(True)
plt.legend(title='Year')
plt.tight_layout()
plt.show()
