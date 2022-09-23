#!/usr/bin/env python
# coding: utf-8

# # Numpy Array

# In[1]:


my_list = [1,2,3]


# In[2]:


import numpy as np


# In[3]:


arr = np.array(my_list)


# In[4]:


arr


# In[5]:


mat = [[1,2,3],[4,5,6],[7,8,9]]


# In[6]:


np.array(mat)


# In[8]:


np.arange(0,10)


# In[10]:


np.arange(0,11,2)


# In[11]:


np.zeros(3)


# In[12]:


np.zeros((2,3))


# In[13]:


np.ones(4)


# In[14]:


np.ones((3,4))


# In[15]:


np.linspace(0,5,10)


# In[16]:


np.eye(4)


# In[17]:


np.random.rand(5)


# In[18]:


np.random.rand(5,5)


# In[21]:


np.random.randn(2)


# In[22]:


np.random.randn(4,4)


# In[23]:


np.random.randint(1,100)


# In[26]:


arr = np.random.randint(1,100,10)


# In[27]:


arr


# In[28]:


arr.max()


# In[30]:


arr.argmax() #location of max value


# In[32]:


arr.argmin() #location of min value


# In[33]:


# data type in the array


# In[34]:


arr.dtype


# In[35]:


# import rand Int


# In[36]:


from numpy.random import randint


# In[38]:


randint(2,10)


# In[ ]:




