#!/usr/bin/env python
# coding: utf-8

# In[4]:



def add(a,b):
    s=a+b
    print("Sum :",s)

def sub(a,b):
    s=a-b
    print("Difference =",s)
    
def mult(a,b):
    m=a*b
    print("product=",m)
    
def div(a,b):
    d=a/b
    print("quotient =",d)
    
def mod(a,b):
    m=a%b
    print("Reminder=",m)
    
    
    
a=int(input("Enter a number:"))
b=int(input("Enter another number:"))
print("1.Add\n2.subtract\n3.multiplication\n4.division\n5.Modulus")
ch=int(input("Enter your operation:"))
if(ch==1):
    add(a,b)
elif(ch==2):
    sub(a,b)
elif(ch==3):
    mult(a,b)
elif(ch==4):      
    div(a,b)
elif(ch==5):        
    mod(a,b)
else:
    print("Invalid")
        
   
 
        
        


# In[ ]:




