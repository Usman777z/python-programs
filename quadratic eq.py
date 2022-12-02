#!/usr/bin/env python
# coding: utf-8

# In[3]:


import cmath as math
a=int(input("Enter value:"))
b=int(input("Enter value:"))
c=int(input("Enter value:"))
d=(b**2)-4*a*c
sol1=(-b+(math.sqrt(d))/(2*a))
sol2=(-b-(math.sqrt(d))/(2*a))
print("Roots of the equation are:",sol1,sol2)


# In[ ]:




