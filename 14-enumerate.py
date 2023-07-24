#!/usr/bin/env python
# coding: utf-8

# In[7]:


# Exercise 1: Write a function called find_vowels that takes a string as input and returns a list of tuples containing the vowel and its index in the string.

def find_vowels(input_string):
    vowels = 'aeiou'
    result = [(letter, index) for index, letter in enumerate(input_string) if letter.lower() in vowels]
    return result

sentence = "Hello python"
result = find_vowels(sentence)


# In[8]:


print(result)


# In[17]:


# Exercise 2: Create a function remove_duplicates that takes a list as input and returns a new list with duplicates removed. Use enumerate to keep track of the elements and their indices.

def remove_duplicates(input_list):
    unique_elements = []
    for index, element in enumerate(input_list):
        if element not in input_list[:index]:
            unique_elements.append(element)
    return unique_elements

numbers = [1, 2, 3, 2, 2, 5, 3, 6]
result = remove_duplicates(numbers)
print(result)


# In[ ]:




