import pandas as pd
import matplotlib.pyplot as plt

elections_df = pd.read_csv('/Users/sabiqadar/Desktop/zainab-portfolio/pandas_activity/US-2016-primary.csv',sep=";")


print(elections_df.head(3))


#average votes by state
avg_votes = elections_df.groupby('state')['votes'].mean().reset_index()
plt.figure(figsize=(12,6))
plt.bar(avg_votes['state'], avg_votes['votes'], color='skyblue')
plt.xlabel('State')
plt.ylabel('Average Votes')
plt.title('Average Votes by State in US 2016 Primary Elections')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

#total votes by candidate
total_votes = elections_df.groupby('candidate')['votes'].sum().reset_index()
plt.figure(figsize=(10,6))
plt.bar(total_votes['candidate'], total_votes['votes'], color='lightgreen')
plt.xlabel('Candidate')
plt.ylabel('Total Votes')
plt.title('Total Votes by Candidate in US 2016 Primary Elections')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#fraction of particular candidate's votes in each state
#allows user to input candidate name - need to spell correctly as in dataset

candidate_name = input('Enter candidate name: ')

candidate_data = elections_df[elections_df['candidate'] == candidate_name]
plt.figure(figsize=(12,6))
plt.bar(candidate_data['state'], candidate_data['fraction_votes'], color='orchid')
plt.xlabel('State')
plt.ylabel('Fraction of Votes')
plt.title(f'Fraction of Votes for {candidate_name} by State in US 2016 Primary Elections')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
