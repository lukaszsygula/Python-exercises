#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Exercise 1: Write a function sum_numbers that takes any number of arguments and returns their sum.

def sum_numbers(*args):
    return sum(args)

result = sum_numbers(10, 53, 29)


# In[4]:


print(result)


# In[14]:


# Exercise 2: Write a function print_info that takes any number of keyword arguments (name, age, occupation, city) and prints them to the screen.

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_info(name='Lukasz', age=28, occupation='data science', city='New York City')


# In[15]:


# Exercise 3: Write a function find_max that takes any number of arguments and returns the largest value among them.

def find_max(*args):
    return max(args)

result = find_max(10, 20, 38, 9, 4, 24)


# In[16]:


print(result)


# In[ ]:




