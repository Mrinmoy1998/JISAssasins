#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Q.no:19

def checkValidity(a, b, c):  
        
    if (a + b <= c) or (a + c <= b) or (b + c <= a) : 
        return False
    else: 
        return True        
   
a = 7
b = 10
c = 5
if checkValidity(a, b, c): 
    print("Valid")  
else: 
    print("Invalid") 


# In[ ]:




