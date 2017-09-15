
# coding: utf-8

# # Rock, Paper and Scissors

# In[1]:


import sys
import time

from flask import Flask, render_template, request
from ipywidgets import widgets
from IPython.display import display
from random import randint
from wtforms import Form


# ## Regeln

# In[2]:


domain = ["rock","paper","scissors"]
result_p1_wins = "Player 1 wins!"
result_p2_wins = "Player 2 wins!"


# In[3]:


def game_logic(player_1, player_2):
    if player_1 in domain and player_2 in domain:

        if player_1 == player_2:
            return("No winner!")
        else:        
            if player_1 == "paper":
                if player_2 == "rock":
                    return(result_p1_wins)
                else:
                    return(result_p2_wins)

            if player_1 == "rock":
                if player_2 == "scissors":
                    return(result_p1_wins)
                else:
                    return(result_p2_wins)    

            if player_1 == "scissors":
                if player_2 == "paper":
                    return(result_p1_wins)
                else:
                    return(result_p2_wins)
    else:
        return("Random error")


# In[4]:


def label_2_int(lbl):
    return {
        'rock': 0,
        'paper': 1,
        'scissors': 2
    }[lbl]


# In[5]:


def int_2_label(nmbr):
    return {
        0: 'rock',
        1: 'paper',
        2: 'scissors'
    }[nmbr]


# In[6]:


def random_play():
    number = randint(0, len(domain) - 1)
    label = int_2_label(number)
    return label;


# In[7]:


def play(player_choice):
    print('We play ' + str(num_rounds) + ' round(s) of Rock-Paper-Scissors. Press r for rock, p for paper or s for scissors within the next 3 seconds.')
    for n in range(num_rounds):
        for i in range(3, 0, -1):
            time.sleep(1)
            print(' ' + str(i))
    


# In[8]:


def play_series(player_1, player_2):
    player_1_wins = 0
    player_2_wins = 0
    for i in range(len(player_1)):
        result = game_logic(player_1[i],  player_2[i])
        print(str(i) + ' | player 1: ' + player_1[i] + '\t player 2: ' + player_2[i] + '\t | ' + result)
        if (result == result_p1_wins):
            player_1_wins = player_1_wins + 1
        if (result == result_p2_wins):
            player_2_wins = player_2_wins + 1     
    print('\nplayer 1: ' + str(player_1_wins) + ' win(s)\t player 2: ' + str(player_2_wins) + ' win(s)') 


# In[9]:


def play_game(player_1):
    player_2 = [random_play() for i in range(len(player_1))]
    play_series(player_1, player_2)


# ### Testing

# In[10]:


game_logic("paper","rock")


# In[11]:


game_logic("scissors", "rack")


# In[12]:


game_logic("scissors", "rock")


# In[13]:


play_series(['rock', 'paper', 'scissors'], ['paper', 'rock', 'rock'])


# In[14]:


label_2_int('rock')


# In[15]:


int_2_label(0)


# In[16]:


random_play()


# In[17]:


play_game(['rock', 'paper', 'scissors'])


# In[18]:


play_game(['scissors', 'rock', 'rock', 'rock', 'paper'])


# ## Play !

# In[19]:


play_game(['paper','rock','rock','scissors','scissors','paper','paper'])


# In[ ]:




