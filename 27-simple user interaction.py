#!/usr/bin/env python
# coding: utf-8

# In[1]:


game_list = [0,1,2]


# In[17]:


def display_game(game_list):
    print("Here is the current list: ")
    print(game_list)


# In[15]:


display_game(game_list)


# In[4]:


def position_choice():
    
    choice = "WRONG"
    
    while choice not in ['0', '1', '2']:
                        
        choice = input("Pick a position (0,1,2): ")
        
        if choice not in ['0', '1', '2']:
            print("Sorry, invalid choice! ")
            
    return int(choice)


# In[6]:


position_choice()


# In[7]:


def replacement_choice(game_list, position):
    
    user_placement = input("Type a string to place at position: ")
    
    game_list[position] = user_placement
    
    return game_list


# In[13]:


replacement_choice(game_list,1)


# In[24]:


def gameon_choice():
    
    choice = "WRONG"
    
    while choice not in ['Y', 'N']:
                        
        choice = input("Keep playing? (Y or N) ")
        
        if choice not in ['Y', 'N']:
            print("Sorry, I dont understand, please choice Y or N ")
            
    if choice == 'Y':
        return True
    else:
        return False


# In[27]:


gameon_choice()


# In[29]:


game_on = True
game_list = [0,1,2]

while game_on:
    
    display_game(game_list)
    
    position = position_choice()
    
    game_list = replacement_choice(game_list, position)
    
    display_game(game_list)
    
    game_on = gameon_choice()
    


# In[ ]:




