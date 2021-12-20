#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import the necessary modules
import matplotlib.pyplot as plt
import pandas as pd


# In[2]:


# Initialize the lists for X and Y
data = pd.read_csv('HMS_Test.csv')
print(data)
data.head()


# In[3]:


#Counting the values of each Incident
count=data['Incident Type'].value_counts()
print(count)


# In[4]:


#Plotting Pie
count.head()
plt.pie(count, labels = count)


# In[8]:


# Genrating Output
plt.show()

