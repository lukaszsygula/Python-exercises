#!/usr/bin/env python
# coding: utf-8

# In[113]:


# CARD
# SUIT, RANK, VALUE
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {"Two": 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}


# In[114]:


class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return self.rank + " of " + self.suit


# In[115]:


three_of_clubs = Card("Clubs", "Three")


# In[116]:


three_of_clubs.suit


# In[117]:


two_hearts = Card("Hearts", "Two")


# In[118]:


print(two_hearts)


# In[119]:


two_hearts.suit


# In[120]:


two_hearts.rank


# In[121]:


class Deck:
    
    def __init__(self):
        
        self.all_cards = []
        
        for suit in suits:
            for rank in ranks:
                # Create the card object
                created_card = Card(suit,rank)
                
                self.all_cards.append(created_card)
                
    def shuffle(self):
        
        random.shuffle(self.all_cards)
        
    def deal_one(self):
        return self.all_cards.pop()


# In[122]:


new_deck = Deck()


# In[123]:


new_deck.shuffle()


# In[124]:


mycard = new_deck.deal_one()


# In[125]:


print(mycard)


# In[126]:


len(new_deck.all_cards)


# In[127]:


bottom_card = new_deck.all_cards[-1]


# In[128]:


print(bottom_card)


# In[129]:


print(new_deck.all_cards[-1])


# In[142]:


class Player:
    
    def __init__(self,name):
        
        self.name = name
        self.all_cards = []
        
    def remove_one(self):
        return self.all_cards.pop(0)
    
    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)
    
    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'


# In[143]:


new_player = Player('Jose')


# In[144]:


print(new_player)


# In[145]:


new_player.add_cards(mycard)


# In[146]:


print(new_player)


# In[147]:


print(mycard)


# In[148]:


new_player.add_cards([mycard,mycard,mycard])


# In[149]:


print(new_player)


# In[150]:


new_player.remove_one()


# In[151]:


print(new_player)


# In[ ]:




