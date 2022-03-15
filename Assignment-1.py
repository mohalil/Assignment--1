#!/usr/bin/env python
# coding: utf-8

# In[1]:


x,y = 0,1
while y<50:
    print(y,end=(" "))
    x,y = y,x+y


# In[2]:


str = "Edyoda"
print(str[::-1])


# In[18]:


numbers = (1,2,3,4,5,6,7,8,9)
count_odd = 0
count_even = 0
for x in numbers:
     if not x%2:
        count_even+=1
else:
        count_odd+=1
print("Number of even numbers:",count_even)
print("Number of odd numbers:",count_odd)


# In[ ]:





# In[ ]:





# In[ ]:




