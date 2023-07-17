#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Program to calculate the sum of numbers in a given list

def calculate_sum(numbers):
    sum = 0
    for num in numbers:
        sum += num
    return sum

# Test case
numbers = [1, 2, 3, 4, 5]
total_sum = calculate_sum(numbers)
print("Sum:", total_sum)


# In[ ]:




