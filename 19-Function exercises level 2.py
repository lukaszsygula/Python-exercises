#!/usr/bin/env python
# coding: utf-8

# In[86]:


# Exercise 1: Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

def has_33(nums):
    for i in range(0, len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

numbers = [1, 3, 5, 5, 2, 3, 3]
result = has_33(numbers)
print(result)


# In[87]:


# Exercise 2: Given a string, return a string where for every character in the original there are three characters

def paper_doll(word):
    word_three_times = ""
    
    for char in word:
        word_three_times += char*3
    return word_three_times

result = paper_doll('Hello')
print(result)


# In[92]:


# Exercise 3: BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'

def blackjack(a, b, c):
    if sum([a, b, c]) <= 21:
        return sum([a, b, c])
    elif 11 in [a, b, c] and sum([a, b, c]) <= 31:
        return sum([a, b, c]) - 10
    else:
        return "BUST"

result = blackjack(5, 6, 7)
print(result)


# In[104]:


# Exercise 4: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.

def summer_69(arr):
    total = 0
    add = True

    for num in arr:
        if add:
            if num != 6:
                total += num
            else:
                add = False
        else:
            if num == 9:
                add = True

    return total

numbers = [4, 5, 6, 7, 8, 9]
result = summer_69(numbers)
print(result)


# In[ ]:




