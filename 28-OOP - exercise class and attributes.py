#!/usr/bin/env python
# coding: utf-8

# In[4]:


class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def say_hello(self):
        print(f"Hello my name is {self.name} and I'm {self.age} years old")

person1 = Person(name='Emma', age=20)
person2 = Person(name='Angelina', age=21)


# In[6]:


person1.say_hello()
person2.say_hello()


# In[ ]:




