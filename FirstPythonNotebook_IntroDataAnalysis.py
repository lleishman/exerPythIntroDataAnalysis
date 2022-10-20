#!/usr/bin/env python
# coding: utf-8

# # First Python Notebook - Introduction to Data Analysis
# 
# * Follow the tutorial at https://www.youtube.com/watch?v=a9UrKTVEeZA&list=PLG9A6ovzPqX6d9uWzx0UYN9pm0zzl5ofA&index=13&t=0s

# In[1]:


import pandas as pd


# In[2]:


from matplotlib import pyplot as plt


# In[3]:


x = [1,2,3]
y = [1,4,9]
z = [10,5,0]
plt.plot(x, y)
plt.plot(x, z)
plt.title("test plot")
plt.xlabel("x")
plt.ylabel("y and z")
plt.legend(["this is y", "this is z"])
plt.show()


# In[4]:


sample_data = pd.read_csv('sample_data.csv')
sample_data
type(sample_data)
sample_data.column_c
type(sample_data.column_c)


# In[5]:


plt.plot(sample_data.column_a, sample_data.column_b, 'o')
plt.plot(sample_data.column_a, sample_data.column_c)
plt.show ()


# In[6]:


data = pd.read_csv('countries.csv')


# In[7]:


data


# In[8]:


# Compare the population growth in the US and China


# In[9]:


data[data.country == 'United States']


# In[12]:


us = data[data.country == 'United States']


# In[13]:


china = data[data.country == 'China']


# In[14]:


china


# In[15]:


plt.plot(us.year, us.population/ 10**6)
plt.plot(china.year, china.population / 10**6)
plt.legend(['United States', 'China'])
plt.xlabel('year')
plt.ylabel('population')
plt.show()


# In[16]:


us.population


# In[17]:


us.population / us.population.iloc[0] * 100


# In[20]:


plt.plot(us.year, us.population / us.population.iloc[0] * 100)
plt.plot(china.year, china.population / china.population.iloc[0] * 100)
plt.legend(['United States', 'China'])
plt.xlabel('year')
plt.ylabel('population growth (first year = 100)')
plt.show()

