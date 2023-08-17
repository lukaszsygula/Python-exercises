#!/usr/bin/env python
# coding: utf-8

# In[9]:


# Exercise 1:

class Product():
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def calculate_total_price(self):
        return self.price * self.quantity
        
    def display_info(self):
        print(f"{self.name}: {self.price} * {self.quantity}")
        
product1 = Product(name="Laptop", price=900, quantity=3)
product2 = Product(name="Smartphone", price=349, quantity=10)
product3 = Product(name="Tablet", price=699, quantity=5)

product1.display_info()
total_price = product1.calculate_total_price()
print("Total price: ", total_price)


# In[22]:


# Exercise 2:
    
class BankAccount():
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance.")
    
    def display_balance(self):
        print(f"Current balance: {self.balance}")
        
    def display_account_info(self):
        print(f"Account Number: {self.account_number}\nBalance {self.balance}")
    

account1 = BankAccount(account_number=123456789, balance=1000)
account2 = BankAccount(account_number=987654321, balance=500)

account1.display_account_info()
account1.deposit(300)
account1.withdraw(600)
account1.display_balance()


# In[26]:


# Exercise 3:

class Customer():
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        
    def display_full_name(self):
        print(f"{self.first_name} {self.last_name}")
        
    def display_contact_info(self):
        print(f"{self.email}")
        
customer1 = Customer(first_name='Emma', last_name='Wotson', email='emma.wotson@gmail.com')
customer2 = Customer(first_name='Angelina', last_name='Jolie', email='angelina.jolie@gmail.com')

customer1.display_full_name()
customer1.display_contact_info()


# In[ ]:




