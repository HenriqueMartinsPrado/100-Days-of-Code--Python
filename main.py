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

# First random number to get a random data inside the list
x = random.randint(0, list_size)

print("Compare A:", game_data.data[x]["name"], ", a", game_data.data[x]["description"], ", from", game_data.data[x]["country"])

# Second random number to get a random data inside the list
y = random.randint(0, list_size)

# Second logo in the game
print(art.logo_vs)

print("Against B:", game_data.data[y]["name"], ", a", game_data.data[y]["description"], ", from", game_data.data[y]["country"])

choice = input("Who has more followers? Type A or B \n")




