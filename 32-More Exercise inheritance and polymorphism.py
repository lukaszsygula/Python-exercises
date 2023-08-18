#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Exercise 1:

class Animal():
    def make_sound(self):
        pass
    
class Bird(Animal):
    def make_sound(self):
        print("Chirp chirp!")
        
class Dog(Animal):
    def make_sound(self):
        print("Woof woof!")
        
bird = Bird()
dog = Dog()

bird.make_sound()
dog.make_sound()


# In[12]:


# Exercise 2:

class Product():
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    def display_info(self):
        print(f"Product: {self.name} Price: {self.price}")
        
class Electronics(Product):
    def __init__(self, name, price, brand):
        super().__init__(name, price)
        self.brand = brand
        
    def display_info(self):
        print(f"Product: {self.name} Price: {self.price} Brand: {self.brand}")
        
product1 = Product(name="Phone", price=599)
product2 = Product(name="Tablet", price=499)
product3 = Product(name="Laptop", price=799)

electronics1 = Electronics(name="Iphone", price=499, brand="Apple")
electronics2 = Electronics(name="Ipad", price=699, brand="Apple")
electronics3 = Electronics(name="MacBook", price=899, brand="Apple")


product1.display_info()
product2.display_info()
product3.display_info()

electronics1.display_info()
electronics2.display_info()
electronics3.display_info()


# In[25]:


# Exercise 3:

class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds")
    
    def display_balance(self):
        print(f"Account Number: {self.account_number}, Balance: ${self.balance:.2f}")

class SavingsAccount(Account):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate
    
    def apply_interest(self):
        self.balance += self.balance * self.interest_rate
    
class CheckingAccount(Account):
    def __init__(self, account_number, balance, overdraft_limit):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit
    
    def withdraw(self, amount):
        if self.balance + self.overdraft_limit >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds and overdraft limit exceeded")

savings = SavingsAccount(account_number="SAV123", balance=1000, interest_rate=0.05)
checking = CheckingAccount(account_number="CHK456", balance=500, overdraft_limit=200)

savings.deposit(200)
checking.withdraw(700)

savings.apply_interest()
checking.withdraw(800)

savings.display_balance()
checking.display_balance()


# In[ ]:




