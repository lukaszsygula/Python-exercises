#!/usr/bin/env python
# coding: utf-8

# In[5]:


# Exercise 1: Summing numbers from 1 to 10

total = 0
num = 1

while num <= 10:
    total += num
    num += 1
    
print(total)


# In[3]:


# Exercise 2: Printing even numbers less than or equal to 20

num = 2

while num <= 20:
    print(num)
    num += 2


# In[4]:


# Exercise 3: Calculating the factorial of a number

n = 5
factorial = 1

while n > 0:
    factorial *= n
    n-= 1
print(factorial)


# In[4]:


# Exercise 4: Prompting the user for a positive number

user_input = int(input("Enter a number: "))

while user_input <= 0:
    user_input = int(input("The number is not positive"))

print("The number is positive")


# In[2]:


# Exercise 5: Summing numbers entered by the user until zero is entered

num = int(input("Enter a number (enter 0 to finish): "))
total = 0

while num != 0:
    total += num
    num = int(input("Enter the next number (enter 0 to finish): "))
    
print("The sum of the entered numbers is:", total)


# In[3]:


# Exercise 6: Printing powers of 2 until exceeding 1000

power = 1

while power <= 1000:
    print(power)
    power *= 2


# In[ ]:




