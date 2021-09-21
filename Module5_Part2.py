#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Part 2 Module5 Course Work

import pandas as pd
grades_dict = {'Wally': [87, 96, 70], 'Eva': [100, 87, 90], 'Sam': [94, 77, 90], 'Katie': [100, 81, 82], 'Bob': [83, 65, 85]}
   


# In[5]:


grades = pd.DataFrame(grades_dict)


# In[6]:


grades


# In[11]:


grades = pd.DataFrame(grades_dict, index=['Test1', 'Test2', 'Test3'])
grades


# In[10]:


grades['Eva']


# In[12]:


grades.Sam


# In[13]:


grades.loc['Test1']


# In[14]:


grades.iloc[1]


# In[15]:


grades.loc['Test1':'Test3']


# In[16]:


grades.iloc[0:2]


# In[18]:


grades.loc['Test1']


# In[19]:


grades.iloc[0]


# In[20]:


grades.iloc[1]


# In[21]:


grades.at['Test2', 'Eva']


# In[22]:


grades.iat[2,0]


# In[23]:


grades.describe()


# In[24]:


grades.mean()


# In[26]:


grades.sort_index(ascending=False)


# In[27]:


grades.sort_index(axis=1)


# In[ ]:




