#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Exercise 1: Generating Even Numbers

def even_numbers():
    num = 0
    while True:
        yield num
        num += 2


# In[5]:


even_gen = even_numbers()
for _ in range(5):
    print(next(even_gen))


# In[6]:


# Exercise 2: Generating Fibonacci Numbers

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


# In[7]:


fib_gen = fibonacci()
for _ in range(10):
    print(next(fib_gen))


# In[8]:


# Exercise 3: Generating Prime Numbers

def primes():
    num = 2
    prime_list = []
    while True:
        is_prime = all(num % prime != 0 for prime in prime_list)
        if is_prime:
            yield num
            prime_list.append(num)
        num += 1


# In[9]:


prime_gen = primes()
for _ in range(10):
    print(next(prime_gen))


# In[ ]:




