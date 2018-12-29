#!/usr/bin/env python
# coding: utf-8

# In[6]:


#Q.no:09

def firstDigit(n):
  while n>=10:
    n = n / 10;
  return int(n)
def lastDigit(n) :
  return(n%10)
n=98563;
print(firstDigit(n),end = " ")
print(lastDigit(n))


# In[ ]:




