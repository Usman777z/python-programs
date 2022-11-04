#!/usr/bin/env python
# coding: utf-8

# In[6]:


n=int(input("Enter a number:"))
sum=0
temp=n
ord=len(str(n))
while(temp>0):
    d=temp%10
    sum+=d**ord
    temp=temp//10
if(sum==n):
    print("Number is amstrong")
else:
    print("Not amstrong")


# In[ ]:





# In[ ]:




