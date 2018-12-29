#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Q.no:07

num=int(input("enter a number: "))
sum=0
while num>0:
    d=num%10
    num=num//10
    sum+=d
    print("the sum of digits of number is: ",sum)


# In[ ]:




