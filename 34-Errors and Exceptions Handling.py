#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Exercise 1: Write a program that asks the user for two numbers and attempts to divide the first number by the second. Handle the division by zero error using the try, except, and finally constructs. Display the result or an error message, and make sure to properly release resources in the finally block.

try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))
    
    result = num1 / num2
except ZeroDivisionError:
    print("Division by zero is not allowed")
else:
    print(f"The result is: {result}")
finally:
    print("Exiting the program")


# In[4]:


# Exercise 2: Write a program that prompts the user to enter a filename and attempts to read its contents. Handle errors that may occur due to a missing file or other read issues using try, except, and finally. Ensure that file resources are properly released in the finally block.

try:
    filename = input("Enter the filename: ")
    with open(filename, 'r') as file:
        content = file.read()
except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")
except Exception as e:
    print(f"Error: {e}")
else:
    print(f"Content of '{filename}':\n{content}")
finally:
    print("Exiting the program.")


# In[ ]:




