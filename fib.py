#!/usr/bin/env python
# coding: utf-8

# In[7]:


def fib(n):
    
    n1,n2=0,1
    count=0
    if(n==1):
        print("fibnocci series= 1")
    else:
        print("Fibinocci series is:")
        while(count<n):
            print(n1)
            y=n1+n2
            n1=n2
            n2=y
            count=count+1
n= int(input("Enter a number:"))
fib(n)

        


# In[ ]:





# In[ ]:




