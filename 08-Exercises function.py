#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Exercise 1: calculate power

def calculate_power(base, exponent):
    return base ** exponent

print(calculate_power(2, 6))


# In[10]:


# Exercise 2: Find max number

def find_max(numbers):
    return max(numbers)

print(find_max([2, 3, 2, 29, 20, 12]))


# In[16]:


# Exercise 3: Reverse string

def reverse_string(string):
    return string[::-1]

print(reverse_string('python'))


# In[19]:


# Exercise 4: Palindrome

def is_palindrome(string):
    return string == string[::-1]

print(is_palindrome('radar'))


# In[23]:


# Exercise 5: Count vowels

def count_vowels(string):
    vowels = 'aoiueAOIUE'
    return sum(1 for char in string if char in vowels)
        
print(count_vowels('python'))


# In[28]:


# Exercise 6: Prime

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

print(is_prime(6))


# In[ ]:




