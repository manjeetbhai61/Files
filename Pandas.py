#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import math


# In[8]:


df=pd.read_csv('F:\python project/GDP.csv')
df


# In[9]:


df.head()


# In[10]:


df.head(n=10)


# In[11]:


df.tail(n=10)


# In[12]:


df.shape


# In[13]:


df.columns


# In[16]:


df.info()


# In[17]:


df.dtypes


# In[18]:


df.loc[1]


# In[19]:


df.iloc[-1]


# In[20]:


df.iloc[99]


# In[21]:


df.loc[99]


# In[24]:


df.loc[[0,99,999]]


# In[25]:


df.iloc[[0,99,999]]


# In[38]:


subset=df.loc[:,'Level']
print(subset.head())


# In[45]:


df.loc[2,'Level']


# In[54]:


df.iloc[[1,10,19],[0,2,3]]


# In[56]:


print(df.groupby('Level')['Weight'].mean())


# In[57]:


print(df.groupby('Level')['Weight'].median())


# In[62]:


print(df.groupby('Quarter')['Weight'].mean())


# In[ ]:




