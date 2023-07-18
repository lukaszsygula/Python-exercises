#!/usr/bin/env python
# coding: utf-8

# In[6]:


# Exercise 1: Sum of Numbers:

total = 0

for num in range(1,101):
    total += num

print("The sum of numbers from 1 to 100 is:", total)


# In[9]:


# Exercise 2: Multiplication by 2:

power = 2

while power <= 100:
    print(power)
    power *= 2


# In[18]:


# Exercise 3: Counting Characters:

string = 'python programming'
count = 0

for char in string:
    if char == 'a':
        count += 1
    

print("The number of occurrences in the string is:", count)


# In[22]:


# Exercise 4: Counting Vowels:

string = "python programming"
vowels = 'aeiou'
count = 0

for char in string:
    if char.lower() in vowels:
        count += 1
        
print("The sum of vowels in the string is:", count)


# In[32]:


# Exercise 5: String Shift:

string = "python programming"
shifted_string = string[-1] + string[:-1]

print("The shifted string is:", shifted_string)


# In[ ]:




