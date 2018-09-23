
# coding: utf-8

# # NumPy Exercises

# #### Import NumPy as np

# In[1]:


import numpy as np


# #### Create an array of 10 zeros 

# In[2]:


np.zeros(10)


# #### Create an array of 10 ones

# In[3]:


np.ones(10)


# #### Create an array of 10 fives

# In[4]:


5*np.ones(10)


# #### Create an array of the integers from 10 to 50

# In[5]:


np.arange(10,51)


# #### Create an array of all the even integers from 10 to 50

# In[6]:


np.arange(10,51,2)


# #### Create a 3x3 matrix with values ranging from 0 to 8

# In[7]:


np.arange(9).reshape((3,3))


# #### Create a 3x3 identity matrix

# In[8]:


np.eye(3)


# #### Use NumPy to generate a random number between 0 and 1

# In[9]:


np.random.rand()


# #### Use NumPy to generate an array of 25 random numbers sampled from a standard normal distribution

# In[10]:


np.random.randn(25)


# #### Create the following matrix:

# In[11]:


np.random.random_sample((10,10))


# #### Create an array of 20 linearly spaced points between 0 and 1:

# In[12]:


np.linspace(0,1,20)


# Replicate the resulting matrix outputs:

# In[13]:


mat = np.arange(1,26).reshape(5,5)
mat


# In[14]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE


# In[15]:


mat[2:,1:]


# In[16]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE


# In[17]:


mat[3,4]


# In[18]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE


# In[19]:


mat[0:3,1:2]


# In[20]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE


# In[21]:


mat[4]


# In[22]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE


# In[23]:


mat[3:]


# ### Now do the following

# #### Get the sum of all the values in mat

# In[24]:


np.sum(mat)


# #### Get the standard deviation of the values in mat

# In[25]:


np.std(mat)


# #### Get the sum of all the columns in mat

# In[26]:


np.sum(mat,axis=0)

