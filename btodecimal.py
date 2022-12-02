#!/usr/bin/env python
# coding: utf-8

# In[3]:


def bin(n):
    sum=0
    i=len(str(n))
    for j in range(0,i):
        x=n%10
        sum+=x*(2**j)
        n//=10
    print("Decimal number is",sum)
        
        
n=int(input("Enter a binary number"))
bin(n)


# In[ ]:




