import pandas as pd
import matplotlib.pyplot as plt

elections_df = pd.read_csv('/Users/sabiqadar/Downloads/US-2016-primary.csv',sep=";")


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

#votes distribution by party
plt.figure(figsize=(10,6))
plt.hist(elections_df['votes'], bins=30, color='salmon', edgecolor='black') 
plt.xlabel('Votes')
plt.ylabel('Frequency')     
plt.title('Votes Distribution in US 2016 Primary Elections')
plt.tight_layout()
plt.show()