#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd 
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns


# In[19]:


ipl=pd.read_csv("C:\\Users\\prajwal patil\\Downloads\\matches.csv")


# In[20]:


ipl.head()


# In[21]:


ipl.shape


# In[22]:


list(ipl['player_of_match'].value_counts()[0:5].keys())


# In[34]:


plt.figure(figsize=(6,5))    
plt.bar(list(ipl['player_of_match'].value_counts()[0:5].keys()),list(ipl['player_of_match'].value_counts()[0:5]),color='g')
plt.show()


# In[37]:


ipl['result'].value_counts()


# In[38]:


ipl['toss_winner'].value_counts()


# In[40]:


batting_first=ipl[ipl['win_by_runs']!=0]


# In[42]:


batting_first.head()


# In[45]:


plt.figure(figsize=(5,7))
plt.hist(batting_first['win_by_runs'])
plt.title("Distribution of runs")
plt.xlabel('Runs')
plt.show()


# In[47]:


batting_first['winner'].value_counts()


# In[53]:


# top 3 teams who one while batting first
plt.figure(figsize=(6,4))
plt.bar(list(batting_first['winner'].value_counts()[0:3].keys()),list(batting_first['winner'].value_counts()[0:3]),color=['b','y','r'])
plt.show()


# In[54]:


plt.figure(figsize=(7,7))
plt.pie(list(batting_first['winner'].value_counts()),labels=list(batting_first['winner'].value_counts().keys()),autopct='%0.1f%%')
plt.show()


# In[55]:


# teams who won whike chasing the target
batting_second=ipl[ipl['win_by_wickets']!=0]


# In[56]:


batting_second.head()


# In[59]:


plt.figure(figsize=(5,5))
plt.hist(batting_second['win_by_wickets'],bins=30)
plt.show()


# In[60]:


batting_second['winner'].value_counts()


# In[67]:


plt.figure(figsize=(7,4))
plt.bar(list(batting_second['winner'].value_counts()[0:3].keys()),list(batting_second['winner'].value_counts()[0:3]),color=['purple','b','r'])
plt.show()


# In[69]:


plt.figure(figsize=(7,7))
plt.pie(list(batting_second['winner'].value_counts()),labels=(batting_second['winner'].value_counts().keys()),autopct='%0.1f%%')
plt.show()


# In[72]:


ipl['Season'].value_counts()


# In[73]:


ipl['city'].value_counts()


# In[74]:


#how many teams won the matches after winning the toss
np.sum(ipl['toss_winner']==ipl['winner'])


# In[75]:


393/756

