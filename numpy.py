#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# In[3]:


my_list = [1,3,4,5,9,7]
arr = np.array(my_list)
print(arr)


# In[4]:


print(type(arr))


# In[30]:


print(arr.shape)


# In[31]:


print(arr.reshape(1,6))
print(arr.reshape(6,1))


# In[32]:


l1 = [12,15,17]
l2 = [11,88,76]
l3 = [56,54,22]
a =np.array([l1,l2,l3])
print(type(a))
print(a)
print(a.shape)


# In[34]:


print(a.reshape(1,9))
print(a.reshape(9,1))


# In[35]:


l4=[1,2,3,4,5]
l5=[7,8,9,0,1]
l6=[1,3,4,5,6]
l7=[7,7,2,3,4]
b= np.array([l4,l5,l6,l7])
print(b)


# In[36]:


print(b[:,:])


# In[37]:


print(b[2:,1:3])


# In[38]:


print(b[1:,1:])


# In[40]:


print(b[1:3,:2])


# In[41]:


ar4=np.arange(1,20,3)
print(ar4)


# In[50]:


ar7=np.linspace(1,20,10)
print(ar7)


# In[46]:


ar4*2


# In[47]:


ar4%2==0


# In[53]:


ar4[4:8:2]=11
print(ar4)


# In[54]:


ar4[4:]=10
print(ar4)


# In[56]:


print(np.random.randn(3,4))


# In[57]:


print(np.random.rand(3,4))


# In[ ]:




