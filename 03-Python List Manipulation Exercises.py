#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Exercise 1: Reversing a List

mylist = [1, 2, 3, 4, 5]
mylist.reverse()
print(mylist)


# In[4]:


# Exercise 2: Sorting a List

mylist = [4, 2, 3, 1, 5]
mylist.sort()
print(mylist)


# In[6]:


# Exercise 3: Combining Two Lists
    
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combining = list1 + list2
print(combining)


# In[11]:


# Exercise 4: Removing an Element from a List

new_list = [1, 6, 9, 4]
new_list.remove(4)
print(new_list)


# In[12]:


# Exercise 5: Counting Occurrences of an Element in a List

mylist = [1, 3, 1, 5, 2, 2, 4, 2, 1]
count = mylist.count(1)
print(count)


# In[15]:


# Exercise 6: Finding the Index of an Element in a List
mylist = [1, 2, 3, 4, 5, 6]
index = mylist.index(1)
print(index)


# In[17]:


# Exercise 7: Copying a List

mylist = ['a', 'b', 'c', 'd', 'e']
new_list = mylist.copy()
print(new_list)


# In[20]:


# Exercise 8: Checking if a List is Empty
mylist = []
if not mylist:
    print("The list is empty")
else:
    print("The list is not empty")


# In[23]:


# Exercise 9: Adding an element to a list at a specific position

mylist = [1, 2, 3, 4, 5]
mylist.insert(0, 7)
print(mylist)


# In[27]:


# Exercise 10: Removing and returning the last element of a list

mylist = ['a', 'b', 'c', 'd']
last_element = mylist.pop()
print(last_element)
print(mylist)


# In[30]:


# Exercise 11: Removing an element from a list at a specific position

mylist = [1, 2, 3, 4, 5]
del mylist[1]
print(mylist)


# In[33]:


# Exercise 12: Checking if an element exists in a list

mylist = [1, 2, 3, 4, 5]
if 3 in mylist:
    print("The element is exists")
else:
    print("The element is not exists")


# In[35]:


# Exercise 13: Clearing the contents of a list

mylist = [1, 2, 3, 4, 5]
mylist.clear()
print(mylist)


# In[39]:


# Exercise 14: Summing numerical values in a list:

mylist = [1, 2, 3, 4, 5]
total_sum = sum(mylist)
print(total_sum)


# In[ ]:




