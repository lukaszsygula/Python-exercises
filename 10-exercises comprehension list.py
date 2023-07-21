#!/usr/bin/env python
# coding: utf-8

# In[6]:


# Exercise 1: Write a list comprehension to create a list containing the squares of numbers from 1 to 10.

squered_number = [x ** 2 for x in range(1, 11)]
print(squered_number)


# In[8]:


# Exercise 2: Given a list of numbers, create a new list containing only the even numbers from the original list.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [x for x in numbers if x % 2 ==0]

print(even_numbers)


# In[13]:


# Exercise 3: Create a list of uppercase characters from a given string

string_uppercase = [string.upper() for string in 'Hello World']

print(string_uppercase)


# In[21]:


# Exercise 4: Given two lists, create a new list that contains pairs of elements from both lists.

list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'd', 'e']
pairs = [(x, y) for x in list1 for y in list2]

print(pairs)


# In[23]:


# Exercise 5: Generate a list of words from a sentence that have more than 4 letters.

sentence = 'This is a simple sentence with some long words'
words = [word for word in sentence.split() if len(word) > 4]

print(words)


# In[ ]:




