#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Exercise 1: Write a program that asks the user to input three numbers. Then, add those numbers to a list and display the contents of the list.

numbers = []
for i in range(3):
    number = int(input(f"Enter the {i+1}. number: "))
    numbers.append(number)

print("List contents:", numbers)


# In[3]:


# Exercise 2: Write a function add_to_list that takes two arguments: a list and an element to add. The function should use the append() method to add the given element to the list and return the updated list.

def add_to_list(my_list, element):
    my_list.append(element)
    return my_list

numbers = [1, 2, 3]
new_number = 4

result = add_to_list(numbers, new_number)
print(result)


# In[4]:


# Exercise 3: Write a program that creates an empty list and then prompts the user to enter three names. Add those names to the list using the append() method and display the contents of the list.

names = []
for i in range(3):
    name = input(f"Enter the {i+1}. name: ")
    names.append(name)

print("List contents:", names)


# In[ ]:




