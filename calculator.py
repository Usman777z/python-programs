#!/usr/bin/env python
# coding: utf-8

# In[10]:


a=int(input("Enter first number:"))
b=int(input("Enter second number:"))    
print('''Enter your choice:
          1.additon
          2.substraction
          3.multiplication
          4.division''')  
ch=int(input("enter choice:"))
if(ch==1):
      s=a+b
      print("sum:",s)
elif(ch==2):
      s=a-b
      print("difference:",s)
elif(ch==3):
      s=a*b
      print("product:",s)
elif(ch==4):
      s=a/b
      print("quotientis:",s)
else:
      print("invalid")
      
      


# In[ ]:





# In[ ]:




