#!/usr/bin/env python
# coding: utf-8

# In[3]:


def power(b,e):
    if(e==1):
        return b
    else:
        return b*power(b,e-1)
    
b=int(input("Enter base:"))
e=int(input("Enter exponent:"))
print(power(b,e))


# In[ ]:




