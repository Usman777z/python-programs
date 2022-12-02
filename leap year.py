#!/usr/bin/env python
# coding: utf-8

# In[2]:


a=int(input("Enter a year:"))
if a%400==0:
    print(a,"is aleap year")
elif a%4==0 and a%100!=0:
    print(a,"is a leap year")
else:
    print("Not a leap year")


# In[ ]:




