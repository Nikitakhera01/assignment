#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df=pd.read_csv('https://download.bls.gov/pub/time.series/cu/cu.item',
                 sep='\t')


# In[3]:


df
#display the complete dataframe


# In[4]:


df.head()
#display the top 5 rows


# In[5]:


df['item_code']
#display the column 'item_code'


# In[6]:


df[df['display_level']>3]
#all the rows where display level is greater than 3


# In[7]:


df.info()
#display the info about the dataframe


# In[8]:


df.describe()
#numericals values only


# In[9]:


df['sort_sequence'].value_counts()


# In[10]:


df['display_level'].value_counts()


# In[11]:


df.corr


# In[12]:


df.head()


# In[13]:


df['selectable']


# In[14]:


df['selectable'].value_counts()


# In[ ]:




