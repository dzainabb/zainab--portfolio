import pandas as pd
import matplotlib.pyplot as plt
# Load the divorce dataset
divorce_df = pd.read_csv('/Users/sabiqadar/Desktop/zainab-portfolio/graphs_for_presentation/all_data/divorces-per-1000-people.csv')

# Filter for United Kingdom
uk_divorce_df = divorce_df[divorce_df['Entity'] == 'United Kingdom']

# Preview the result
print(uk_divorce_df)


# Load working hours data
hours_df = pd.read_csv('/Users/sabiqadar/Desktop/zainab-portfolio/graphs_for_presentation/all_data/annual-working-hours-per-worker.csv')

# Filter working hours for United Kingdom
uk_hours_df = hours_df[hours_df['Entity'] == 'United Kingdom']

# Merge both datasets on Entity and Year
merged_df = pd.merge(uk_hours_df, uk_divorce_df, on=['Entity', 'Year', 'Code'])

# Preview merged data
print(merged_df)

#make a new csv with merged data
merged_df.to_csv('/Users/sabiqadar/Desktop/zainab-portfolio/graphs_for_presentation/all_data/merged_data.csv', index=False)


