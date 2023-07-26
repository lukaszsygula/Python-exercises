#!/usr/bin/env python
# coding: utf-8

# In[16]:


# Exercise 1: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd

def lesser_of_two_evens(a, b):
    if a % 2 == 0 and b % 2 == 0:
        return min(a, b)
    else:
        return max(a, b)
    
result = lesser_of_two_evens(2, 4)
result2 = lesser_of_two_evens(2, 5)


# In[20]:


print(result, result2)


# In[25]:


# Exercise 2: Write a function takes a two-word string and returns True if both words begin with same letter

def same_letter(word_string):
    word = word_string.split()
    if len(word) != 2:
        return False
    else:
        return word[0][0].lower() == word[1][0].lower()

result1 = same_letter("Apple apricot") 
result2 = same_letter("Hello world")
result3 = same_letter("Horse hotel")


# In[26]:


print(result1, result2, result3)


# In[64]:


# Exercise 3: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False

def makes_twenty(*args):
    if sum(args) == 20 or 20 in args:
        return True
    else:
        return False

result1 = makes_twenty(20, 10)
result2 = makes_twenty(12, 8)
result3 = makes_twenty(2, 3)


# In[65]:


print(result1, result2, result3)


# In[ ]:




