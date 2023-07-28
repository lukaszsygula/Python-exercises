#!/usr/bin/env python
# coding: utf-8

# In[9]:


def master_yoda(text):
    wordlist = text.split()
    reverse_word_list = wordlist[::-1]
    return " ".join(reverse_word_list)


# In[10]:


print(master_yoda('I am home'))


# In[ ]:




