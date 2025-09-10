#!/usr/bin/env python
# coding: utf-8

# PROBLEM #1 

# In[2]:


import pandas as pd


# In[3]:


url = "http://bit.ly/Cars_file"
cars = pd.read_csv(url)


# In[4]:


print("First five rows:")
print(cars.head())


# In[5]:


print("\nLast five rows:")
print(cars.tail())

