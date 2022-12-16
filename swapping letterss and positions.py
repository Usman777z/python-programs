#!/usr/bin/env python
# coding: utf-8

# In[1]:


def change(text1,text2):
    first=text1[0]
    second=text2[0]
    a=list(text1)
    b=list(text2)
    a[0]=second
    b[0]=first
    string1=''.join(a)
    string2=''.join(b)
    final=string1+' '+string2
    return final
    
    
    
word1=input('Enter the first word :')
word2=input('Enter the second word : ')
print("Joined word with swapping letters in first position is:  ",change(word1,word2))


# In[ ]:




