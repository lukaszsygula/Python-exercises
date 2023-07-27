#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Write a function that capitalizes the first and fourth letters of a name 

def capitalize_name(name):
    if len(name) >= 4:
        first_letter = name[0].upper()
        fourth_letter = name[3].upper()
        result = first_letter + name[1:3] + fourth_letter + name[4:]
    else:
        result = name
    return result

name1 = "macdonald"
capitalized_name1 = capitalize_name(name1)

print(capitalized_name1)


# In[ ]:




