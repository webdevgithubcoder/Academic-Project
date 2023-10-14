#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


matches = pd.read_csv('matches.csv') 
# -->This line reads a CSV file named 'matches.csv' and stores its contents in a DataFrame called 'matches'.   
deliveries = pd.read_csv('deliveries.csv')
# -->This line reads a CSV file named 'deliveries.csv'' and stores its contents in a DataFrame called 'deliveries'. 


# In[3]:


matches.head()
# -->we are using the Pandas DataFrame method head(). This method is used to display the first few rows of a DataFrame. By default, it displays the first 5 rows,


# In[4]:


matches.shape
# -->When you use the matches.shape attribute, we're obtaining information about the dimensions of the 'matches' DataFrame. Specifically, it returns a tuple representing the number of rows and columns in the DataFrame.


# In[5]:


deliveries.head()
# -->To display the first few rows of the deliveries DataFrame, you can use the head() method


# In[11]:


total_score_df = deliveries.groupby(['match_id','inning']).sum()['total_runs'].reset_index()
# -->deliveries.groupby(['match_id', 'inning']): This part of the code groups the rows in the deliveries DataFrame by two columns, 'match_id' and 'inning'. This operation creates separate groups of data for each unique combination of 'match_id' and 'inning'.
# -->sum()['total_runs']: Within each group created by the groupby operation, this code sums the values in the 'total_runs' column. So, for each combination of 'match_id' and 'inning', it calculates the total runs scored in that inning during that match.
# -->After performing the grouping and aggregation, this part of the code resets the index of the resulting DataFrame.


# In[12]:


total_score_df =total_score_df[total_score_df['inning'] == 1]
# -->It is filtering the total_score_df DataFrame to only include rows where the 'inning' column has a value of 1


# In[13]:


matches_df = matches.merge(total_score_df[['match_id','total_runs']],left_on = 'id',right_on = 'match_id')
# -->total_score_df[['match_id', 'total_runs']]: This is a subset of the total_score_df DataFrame, containing only the columns 'match_id' and 'total_runs'. It represents the total runs scored in the first inning of each match.
# -->left_on='id' and right_on='match_id': These parameters specify which columns to use as the join keys for the merge operation. The left_on parameter indicates that the 'id' column from the matches DataFrame should be used as the left DataFrame's join key, and the right_on parameter indicates that the 'match_id' column from the subset of total_score_df should be used as the right DataFrame's join key.


# In[ ]:


matches_df


# In[ ]:


matches_df['team1'].unique()


# In[ ]:


teams = [
    'Sunrisers Hyderabad', 
    'Mumbai Indians',
    'Royal Challengers Bangalore',
    'Kolkata Knight Riders',
    'Kings XI Punjab',
    'Chennai Super Kings',
    'Rajasthan Royals', 
    'Delhi Capitals'
]


# In[ ]:


matches_df['team1'] = matches_df['team1'].str.replace('Delhi Daredevils','Delhi Capitals')
matches_df['team2'] = matches_df['team2'].str.replace('Delhi Daredevils','Delhi Capitals')

matches_df['team1']=matches_df['team1'].str.replace('Deccan Chargers','Sunrisers Hyderabad')
matches_df['team2']=matches_df['team2'].str.replace('Deccan Chargers','Sunrisers Hyderabad')
# -->str.replace() method to replace all occurrences of the string "Delhi Daredevils" in the 'team1' column of the matches_df DataFrame with "Delhi Capitals.


# In[ ]:


matches_df = matches_df[matches_df['team1'].isin(teams)]
matches_df = matches_df[matches_df['team2'].isin(teams)]
# -->It is filtering the matches_df DataFrame to only include rows where the 'team1' column contains values that are present in a list or Series named 'teams


# In[ ]:


matches_df.shape


# In[ ]:


matches_df =matches_df[matches_df['dl_applied'] == 0]
# -->This operation removes rows where the Duckworth-Lewis (DL) method was applied during the match


# In[15]:


matches_df = matches_df[['match_id','city','winner','total_runs']]
# -->It is selecting specific columns from the matches_df DataFrame and creating a new DataFrame with only those columns


# In[ ]:


deliveries_df = matches_df.merge(deliveries,on = 'match_id')
# -->It is performing a merge operation between the matches_df DataFrame and the deliveries DataFrame using the 'match_id' column as the merge key. 


# In[ ]:


deliveries_df = deliveries_df[deliveries_df['inning'] == 2]
# -->It is filtering the deliveries_df DataFrame to only include rows where the 'inning' column has a value of 2. This operation keeps only the data related to the second inning of matches.


# In[17]:


deliveries_df.shape


# In[ ]:




