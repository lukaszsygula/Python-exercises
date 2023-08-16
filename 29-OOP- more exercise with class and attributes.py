#!/usr/bin/env python
# coding: utf-8

# In[31]:


# Exercise 1:

class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        
    def display_info(self):
        print(f"{self.year} {self.make} {self.model}")

car1 = Car(make='Toyota', model='Auris', year=2016)
car2 = Car(make='Ford', model='Focus', year=2015)
car3 = Car(make='Honda', model='Civic', year=2022)

car1.display_info()
car2.display_info()
car3.display_info()


# In[4]:


# Exercise 2:

class Animal():
    def __init__ (self, species, sound):
        self.species = species
        self.sound = sound
        
    def make_sound(self):
        print(f"The {self.species} makes a {self.sound} sound.")

dog = Animal(species="dog", sound="bark")
cat = Animal(species="cat", sound="meow")

dog.make_sound()
cat.make_sound()


# In[16]:


# Exercise 3:

class Calculator():
    def __init__(self, initial_value=0):
        self.result = initial_value
    
    def add(self, value):
        self.result += value
    
    def subtract(self, value):
        self.result -= value
        
    def multiply(self, value):
        self.result *= value
    
    def divide(self, value):
        if value != 0:
            self.result /= value
        else:
            print("Can not divide by 0")
        
calculator = Calculator()

calculator.add(50)
calculator.subtract(10)
calculator.multiply(5)
calculator.divide(2)

print("Final result: ", calculator.result)


# In[22]:


# Exercise 4:

class Book():
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    
    def display_info(self):
        print(f"{self.title}: {self.author} ({self.year})")

book1 = Book(title="Harry Potter", author="J.K. Rowling", year=1997)
book2 = Book(title="Lord of the Rings", author="J.R.R. Tolkien", year=1954)

book1.display_info()
book2.display_info()


# In[ ]:




