#!/usr/bin/env python
# coding: utf-8

# In[8]:


# Exercise 1: Simple Calculator

def calculator(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        return a / b
    else:
        return ("Invalid operator")

print(calculator(5, 3, '+'))
print(calculator(10, 4, '-'))
print(calculator(5, 24, '*'))
print(calculator(10, 2, '/'))


# In[ ]:




