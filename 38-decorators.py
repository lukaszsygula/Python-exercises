#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Exercise: Tracking Function Execution Time

import time

def measure_time(function):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = function(*args, **kwargs)
        end = time.time()
        print(f"Execution time of '{function.__name__}': {end - start} seconds")
        return result
    return wrapper

@measure_time
def calculations():
    total = 0
    for i in range(1000000):
        total += i
    return total

print(calculations())


# In[ ]:




