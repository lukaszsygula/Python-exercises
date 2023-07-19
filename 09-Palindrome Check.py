#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Exercise: Palindrome Check

def is_palindrome(word):
    word = word.lower().replace(" ", "")
    return word == word[::-1]

print(is_palindrome("radar"))
print(is_palindrome("python"))
print(is_palindrome("Able was I ere I saw Elba"))


# In[ ]:




