#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Importing the dependencies
import pandas as pd


# In[2]:


#Read the csv data
df = pd.read_csv('election_data.csv')
df.head()


# In[6]:


#The total number of votes cast
total_count = df['Ballot ID'].nunique()
print(total_count)


# In[7]:


# A complete list of candidates who received votes
candidate_list = df['Candidate'].unique()
print(candidate_list)


# In[12]:


# The percentage of votes each candidate won
# The total number of votes each candidate won
charles_vote = df[df['Candidate'] == 'Charles Casper Stockham']['Ballot ID'].nunique()
diana_vote = df[df['Candidate'] == 'Diana DeGette']['Ballot ID'].nunique()
raymon_vote = df[df['Candidate'] == 'Raymon Anthony Doane']['Ballot ID'].nunique()
charles_pcnt = charles_vote / total_count
diana_pcnt = diana_vote / total_count
raymon_pcnt = raymon_vote / total_count


# In[15]:


# The winner of the election based on popular vote
vote_counts = pd.Series(data={'Charles Casper Stockham': charles_vote,
                              'Diana DeGette': diana_vote,
                              'Raymon Anthony Doane': raymon_vote})
winner = vote_counts.idxmax()
print(winner)


# In[ ]:


#Election results report
with open("pypoll_report.txt", "w") as file:
    file.write('Election Results')
    file.write('-'*20)
    file.write('Total Votes: ' + str(total_count))
    file.write('-'*20)
    file.write('Charles Casper Stockham: ' +str(charles_pcnt)+'% ' +str(charles_vote))
    file.write('Diane DeGette: ' +str(diana_pcnt)+'% ' +str(diana_vote))
    file.write('-'*20)
    file.write('Winner: '+ str(winner))
    file.write('-'*20)
file.close()


