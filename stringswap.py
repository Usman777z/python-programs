#!/usr/bin/env python
# coding: utf-8

# In[1]:


def swap(string):
    start=string[0]
    end=string[-1]
    swstr=end+string[1:-1]+start
    print(swstr)
a=input("enetr a string:")
swap(a)


# In[ ]:




