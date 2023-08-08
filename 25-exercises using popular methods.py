#!/usr/bin/env python
# coding: utf-8

# In[5]:


# Exercise 1: Write a program that asks the user to input a sentence. Then, split the sentence into words and display them in reverse order.

sentence = input("Enter a sentence: ")
words = sentence.split()
reversed_words = list((reversed(words)))

print(reversed_words)


# In[19]:


# Exercise 2: Write a function count_vowels that takes a string as an argument and returns the number of vowels in that string.

def count_vowels(text):
    count = 0
    vowels = 'aeiou'
    for char in text:
        if char in vowels:
            count += 1
    return count

words = 'python programming'
result = count_vowels(words)
print(result)


# In[21]:


# Exercise 3: Write a program that generates a random number between 1 and 100 and asks the user to guess the number. Display the appropriate message based on the result.

import random

target_number = random.randint(1, 100)
guess = int(input("Guess a number between 1 and 100: "))

while guess != target_number:
    if guess < target_number:
        print("Too low!")
    else:
        print("Too high!")
    guess = int(input("Guess a number between 1 and 100: "))

print("Congratulations, you guessed it!")


# In[ ]:




