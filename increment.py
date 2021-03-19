#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
i = sys.argv[1]
number = int(sys.argv[2])


# In[3]:


def scale_increment(num, scale = 10):
    return(num*scale + 1)


# In[12]:


results = (scale_increment(number))
out_file_name = "results"+str(i)+".txt"
with open(out_file_name, 'w') as f:
    print(results, file=f)


# In[ ]:




