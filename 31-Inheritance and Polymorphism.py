#!/usr/bin/env python
# coding: utf-8

# In[11]:


# Exercise 1: Inheritance

class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    
    def display_info(self):
        print(f"This is a {self.brand} vehicle.")
        
class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model
    
    def display_info(self):
        print(f"This is a {self.brand} {self.model} car.")
        
vehicle = Vehicle(brand='Toyota')
vehicle.display_info()

car = Car('Toyota', 'Corolla')
car.display_info()


# In[14]:


# Exercise 2: Polymorphism

def show_vehicle_info(vehicle):
    vehicle.display_info()
    
vehicle1 = Vehicle("Toyota")
vehicle2 = Car("Toyota", "Auris")

show_vehicle_info(vehicle1)
show_vehicle_info(vehicle2)


# In[ ]:




