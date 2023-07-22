#!/usr/bin/env python
# coding: utf-8

# In[7]:


# Exercise 4: Write a function combine_lists that combines two lists passed as positional arguments and returns the resulting list.

def combine_list(*args):
    return args
    
list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = combine_list(*list1, *list2)


# In[8]:


print(result)


# In[33]:


# Exercise 5: Write a function count_vowels that takes any number of string arguments and returns the sum of all vowels (a, e, i, o, u) present in them.

def count_vowels(*args):
    vowels = 'aeiou'
    total = 0
    for word in args:
        total += sum(1 for letter in word.lower() if letter in vowels)
    return total

result = count_vowels('Hello', 'World', 'Python')


# In[34]:


print(result)


# In[35]:


# Exercise 6: Write a function print_even_numbers that takes a list of numbers and prints only the even ones.

def print_even_numbers(*args):
    even_numbers = [x for x in args if x % 2 == 0]
    return even_numbers


# In[40]:


print(print_even_numbers(1, 2, 3, 4, 5, 6))


# In[ ]:




