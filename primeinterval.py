#!/usr/bin/env python
# coding: utf-8

# In[2]:


a=int(input("enter the limit:"))
b=int(input("Enter the limit:"))
for i in range(a,b+1):
    if(i>1):
        for j in range(2,i):
            if(i%j==0):
                break
        else:
                print(i)


# In[ ]:




