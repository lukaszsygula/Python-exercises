#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Exercise Alternating Case String

def myfunc(*args):
    result = ""
    for word in args:
        for i, letter in enumerate(word):
            if i % 2 == 0:  # Even index (starting from 0) -> Uppercase
                result += letter.upper()
            else:  # Odd index -> Lowercase
                result += letter.lower()
    return result


# In[4]:


print(myfunc("Hello"))


# In[ ]:




