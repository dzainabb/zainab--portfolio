#DIFF COUNTRIES AND DIVORCE AND WORK
import pandas as pd
import matplotlib.pyplot as plt

# Load datasets 
divorce_df = pd.read_csv('/Users/sabiqadar/Desktop/zainab-portfolio/graphs_for_presentation/all_data/divorces-per-1000-people.csv')
hours_df = pd.read_csv('/Users/sabiqadar/Desktop/zainab-portfolio/graphs_for_presentation/all_data/annual-working-hours-per-worker.csv')

# Merge datasets on Entity, Code, and Year
merged_df = pd.merge(
    hours_df, divorce_df,
    on=['Entity', 'Code', 'Year'],
    suffixes=('_hours', '_divorce')
)

# Choose countries to plot
countries = ['United Kingdom', 'United States']  # two countries to compare

# Create figure
fig, ax1 = plt.subplots(figsize=(12,6))

# Colours for each country 
colors = ['tab:blue', 'tab:red']

#  Plot working hours (left)
for i, country in enumerate(countries):
    data = merged_df[merged_df['Entity'] == country]
    ax1.plot(
        data['Year'], data['Working hours per worker'],
        color=colors[i],
        linestyle='-',
        label=f'{country} - Working Hours'
    )

ax1.set_xlabel('Year')
ax1.set_ylabel('Working Hours per Worker')
ax1.tick_params(axis='y', labelcolor='black')

# Plot divorce rate (Right)
ax2 = ax1.twinx()

for i, country in enumerate(countries):
    data = merged_df[merged_df['Entity'] == country]
    ax2.plot(
        data['Year'], data['Crude divorce rate'],
        color=colors[i],
        linestyle='--',
        label=f'{country} - Divorce Rate'
    )

ax2.set_ylabel('Crude Divorce Rate')
ax2.tick_params(axis='y', labelcolor='black')

# Combine legends 
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines + lines2, labels + labels2, loc='upper left', bbox_to_anchor=(1.05, 1))

#Title & layout 
plt.title('Working Hours vs Divorce Rate by Country')
plt.tight_layout()
plt.show()
