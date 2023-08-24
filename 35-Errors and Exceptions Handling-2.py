#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Exercise 1:
try:
    user_input = input("Enter an integer: ")
    number = int(user_input)
except ValueError:
    print(f"Error: '{user_input}' is not a valid integer.")
else:
    print(f"Successfully converted '{user_input}' to an integer: {number}")
finally:
    print("Exiting the program.")


# In[4]:


# Exercise 2:
try:
    with open("data.txt", 'r') as file:
        content = file.read()
        numbers = [int(num) for num in content.split()]
except FileNotFoundError:
    print("Error: File 'data.txt' not found.")
except ValueError:
    print("Error: Cannot convert some values to integers.")
else:
    print("Successfully read and converted data:")
    print(numbers)
finally:
    print("Exiting the program.")


# In[ ]:




