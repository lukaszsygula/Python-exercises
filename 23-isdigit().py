#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Exercise 1: Write a function is_all_digits that takes a string as an argument and returns True if all characters in the string are digits, and False otherwise.

def is_all_digits(text):
    return text.isdigit()

print(is_all_digits("12345"))  
print(is_all_digits("Hello123"))  
print(is_all_digits("42.0"))  


# In[6]:


# Exercise 2: Write a program that asks the user to input a number. Check if the entered string consists only of digits and display the appropriate message.

number = input("Enter a number: ")

if number.isdigit():
    print("This is an intiger")
else:
    print("This is not an intiger")


# In[13]:


# Exercise 3: Write a program that prompts the user to enter three strings. Check if each of the given strings consists only of digits and display the appropriate message for each string.

texts = []

for i in range(3):
    text = input(f"Enter the {i+1}. string ")
    texts.append(text)

for text in texts:
    if text.isdigit():
        print("This is an intiger")
    else:
        print("This is not an intiger")


# In[ ]:




