#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Exercise 3: Write a function find_max_length_word that takes a list of strings as input and returns the longest word along with its index in the list.

def find_max_length_word(input_string):
    max_length_word = []
    max_length_index = -1
    
    for index, word in enumerate(input_string):
        if len(word) > len(max_length_word):
            max_length_word = word
            max_length_index = index

    return max_length_word, max_length_index

fruits = ['banana', 'apple', 'orange']
result_word, result_index = find_max_length_word(fruits)
print(f"The longest word is '{result_word}' at index {result_index}.")


# In[3]:


# Exercise 5: Create a function capitalize_alternate_words that takes a sentence as input and capitalizes every other word in the sentence. Return the modified sentence.

def capitalize_alternate_words(sentence):
    words = sentence.split()
    result = [word.upper() if i % 2 == 0 else word for i, word in enumerate(words)]
    return ' '.join(result)

sentence = "Python is a great programming language"
result = capitalize_alternate_words(sentence)
print(result)
    


# In[ ]:




