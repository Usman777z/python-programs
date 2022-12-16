#!/usr/bin/env python
# coding: utf-8

# In[3]:


a=input("Enter string:")
print("orginal string:"+str(a))
k='$'
res=a[0]+a[1:].replace(a[0],k)
print("New string is::",res)


# In[ ]:


def change(x1,x2):
    first=x1[0]
    second=x2[0]
    a=list(x1)
    b=list(x2)
    a[0]=second
    b[0]=first
    string1=" ".join(a)
    string2=" ".join(b)
    first=string1+' '+string2
    return first
w1=input("Enter first word:")
w2=input("Enter second word:")
print(change(w1,w2))


# In[ ]:




