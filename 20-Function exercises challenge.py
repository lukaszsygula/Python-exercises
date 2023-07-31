#!/usr/bin/env python
# coding: utf-8

# In[9]:


# Exercise 1: SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order

def spy_game(nums):
    
    code = [0,0,7,'x']
    
    for num in nums:
        if num == code[0]:
            code.pop(0)
    return len(code) == 1

numbers = [1,2,4,0,0,7,5]
result = spy_game(numbers)
print(result)


# In[12]:


# Exercise 2: COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number

def count_primes(num):
    if num < 2:
        return 0
    
    primes = [2]
    x = 3
    
    while x <= num:
        for y in range(3,x,2):
            if x % y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
            
    print(primes)
    return len(primes)


# In[13]:


count_primes(100)


# In[ ]:




