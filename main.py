#################################################################
# Day 14

# Higher or Lower Project

import game_data
import art
import random

# Get the size of my list
list_size = len(game_data.data)

# First logo in the game
print(art.logo_higher_lower)

print("Compare A:", game_data.data[0]["name"], ", a", game_data.data[0]["description"], ", from", game_data.data[0]["country"])

# Second logo in the game
print(art.logo_vs)

print("Against B:", game_data.data[0]["name"], ", a", game_data.data[0]["description"], ", from", game_data.data[0]["country"])

choice = input("Who has more followers? Type A or B \n")




