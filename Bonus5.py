#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


zips = pd.Series({'Boston': '02215', 'Miami': '3310'})


# In[3]:


zips


# In[4]:


# Bonus #4

zips.str.match(r'\d{5}')


# In[6]:


# Bonus #5

cities = pd.Series(['Boston, MA 02215', 'Miami, FL 33101'])


# In[7]:


cities


# In[8]:


cities.str.contains(r' [A-Z]{2} ')


# In[9]:


cities.str.match(r' [A-Z]{2} ')


# In[10]:


# Bonus #6

contacts = [['Mike Green', 'demo1@deitel.com', '5555555555'],
                ['Sue Brown', 'demo2@deitel.com', '5555551234']]
    


# In[25]:


contactsdf = pd.DataFrame(contacts,
                               columns=['Name', 'Email', 'Phone'])


# In[26]:


contactsdf


# In[27]:


import re


# In[28]:


def get_formatted_phone(value):
         result = re.fullmatch(r'(\d{3})(\d{3})(\d{4})', value)
         return '-'.join(result.groups()) if result else value


# In[29]:


formatted_phone = contactsdf['Phone'].map(get_formatted_phone)


# In[30]:


formatted_phone


# In[32]:


contactsdf['Phone'] = formatted_phone


# In[33]:


contactsdf


# In[ ]:




