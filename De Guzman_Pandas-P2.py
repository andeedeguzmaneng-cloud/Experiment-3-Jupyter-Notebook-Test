#!/usr/bin/env python
# coding: utf-8

# PROBLEM #2

# In[7]:


import pandas as pd


# In[8]:


url = "http://bit.ly/Cars_file"
cars = pd.read_csv(url)


# In[9]:


odd_columns = cars.iloc[:, ::2]
print("a. First five rows with odd-numbered columns:")
print(odd_columns.head())


# In[10]:


print("\nb. Row for 'Mazda RX4':")
print(cars[cars['Model'] == 'Mazda RX4'])


# In[11]:


camaro_cyl = cars[cars['Model'] == 'Camaro Z28']['cyl'].values[0]
print(f"\nc. 'Camaro Z28' has {camaro_cyl} cylinders.")


# In[12]:


models = ['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic']
selected = cars[cars['Model'].isin(models)][['Model', 'cyl', 'gear']]
print("\nd. Cylinders and gear types for selected models:")
print(selected)


# In[ ]:




