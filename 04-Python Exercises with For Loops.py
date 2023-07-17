#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Exercise 1: Printing the elements of a list

my_list = [1, 2, 3, 4, 5]
for element in my_list:
    print(element)


# In[7]:


# Exercise 2: Calculating the sum of elements in a list

my_list = [1, 2, 6, 4, 5, 6, 7, 8]
total_sum = 0
for element in my_list:
    total_sum += element
print(total_sum)


# In[12]:


# Exercise 3: Displaying the indexes and values of elements in a list

mylist = ['a', 'b', 'c', 'd', 'e']
for index, value in enumerate(mylist):
    print(f"Index: {index}, Value {value}")


# In[18]:


# Exercise 4: Generating a list of even numbers

even_number = []
for num in range(1, 11):
    if num % 2 == 0:
        even_number.append(num)
print(even_number)


# In[23]:


# Exercise 5: Iterating through a dictionary and displaying keys and values

my_dict = {'a': 1, 'b': 2, 'c': 3}
for key, value in my_dict.items():
    print(f"Key {key}, Value {value}")


# In[24]:


# Exercise 6: Displaying characters in a string

my_string = "Hello World!"
for char in my_string:
    print(char)


# In[ ]:




