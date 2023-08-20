#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Exercise 1: __str__

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    
    def __str__(self):
        return f"{self.name} is {self.age} years old."

person = Person("Alice", 30)
print(str(person))


# In[10]:


# Exercise 2: __len__

class MyList:
    def __init__(self, items):
        self.items = items
    
    def __len__(self):
        return len(self.items)

my_list = MyList([1, 2, 3, 4, 5])
print(len(my_list))


# In[8]:


# Exercise 3: __del__

class File:
    def __init__(self, filename):
        self.filename = filename

    def __del__(self):
        print(f"Deleting file: {self.filename}")

file = File("example.txt")
del file


# In[ ]:




