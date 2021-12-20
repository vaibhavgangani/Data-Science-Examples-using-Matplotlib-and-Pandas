#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import the necessary modules
import matplotlib.pyplot as plt


# In[2]:


# Import the necessary modules
import pandas as pd


# In[3]:


# Initialize the lists for X and Y
data = pd.read_csv('HMS_Test.csv')
print(data)


# In[4]:



#Plotting Bar
y = data["Priority"].value_counts()
x = data["Priority"].value_counts().keys()
plt.title("Priority Bar Chart")
plt.ylabel("Total Count")
plt.xlabel("Number of Values")


# In[5]:


# Generating Output
plt.bar(x, y)
plt.show()

