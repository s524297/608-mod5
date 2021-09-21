#!/usr/bin/env python
# coding: utf-8

# In[23]:


import pandas as pd


# In[24]:


grades = pd.Series([87, 100, 94])


# In[25]:


grades


# In[26]:


grades[0]


# In[27]:


grades.count()


# In[28]:


grades.mean()


# In[29]:


grades.min()


# In[30]:


grades.max()


# In[31]:


grades.std()


# In[32]:


#Dictionary Initializers 

grades = pd.Series({'Wally': 87, 'Eva': 100, 'Sam': 94})


# In[33]:


grades


# In[34]:


grades['Eva']


# In[35]:


grades


# In[36]:


grades.Wally
