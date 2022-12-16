#!/usr/bin/env python
# coding: utf-8

# In[3]:


def rec_fact(n):
    if n==1:
        return n
    else:
        return n*rec_fact(n-1)
 
n=int(input("Enter a number:"))
f=rec_fact(n)
print("Factorial=",f)


# In[ ]:




