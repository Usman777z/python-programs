#!/usr/bin/env python
# coding: utf-8

# In[ ]:


try:
    
    num=int(input("Enter a number:"))
    if(num<0):        
        raise ValueError("that is a negative number")
except ValueError as e:
    print(e)


# In[ ]:





# In[ ]:




