#!/usr/bin/env python
# coding: utf-8

# In[1]:


def get_number_in_range():
    while True:
        try:
            number = int(input("Please enter a number between 0 and 10: "))
            if 0 <= number <= 10:
                return number
            else:
                print("Number is not in the range 0-10. Try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

user_number = get_number_in_range()
print("You entered:", user_number)


# In[ ]:




