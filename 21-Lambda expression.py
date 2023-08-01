#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Exercise 1: Write a function that squares each element of a list using a lambda expression and the map function
numbers = [1, 2, 3, 4, 5]
squered_numbers = list(map(lambda x: x * 2, numbers))
print(squered_numbers)


# In[7]:


# Exercise 2: Write a function that returns True if the length of a given string is even, and False otherwise, using a lambda expression and the len function

is_even_length = lambda word: len(word)

print(is_even_length('programming'))


# In[17]:


# Exercise 3: Write a function that returns the sum of two numbers, but only if both numbers are positive, using a lambda expression and the filter function

numbers = [2, 4, 3, 1, 9, 6]
sum_positive = sum(filter(lambda x: x > 0, numbers))
print(sum_positive)


# In[28]:


# Exercise 4: Write a function that sorts a list of strings based on their length using a lambda expression and the sorted function

words = ['programming', 'python', 'lambda', 'expresion', 'map', 'filter']
words_length = sorted(words, key=lambda word: len(word))
print(words_length)


# In[29]:


# Exercise 5: Write a function that returns the number of vowels in a given string using a lambda expression and the filter function

text = 'python programming'
vowels = 'aeiou'
vowel_count = len(list(filter(lambda letter: letter.lower() in vowels, text)))
print(vowel_count)


# In[ ]:




