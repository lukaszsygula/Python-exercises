#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Exercise: Factorial Calculation

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))
print(factorial(8))
print(factorial(3))


# In[ ]:




