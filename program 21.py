#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:


def fib(n):
    if(n <= 1):
        return n
    else:
        return(fib(n-1) + fib(n-2))
n = int(input("Enter number of terms:"))
print("Fibonacci sequence:")
for i in range(n):
    print(fib(i))


# In[ ]:




