
from art import logo
import random

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a the number between 1 and 100.")
level = input("Choose a diffilculty. Type 'easy' or 'hard': ")

answer = random.randint(1, 100)

level_opt = {"easy": 5, "hard": 10}
is_gameover = False

print(level_opt["easy"])

# def check_level(level):
#   if level in level_opt:
#     print("Easy")
    
  # elif level_opt[level] == level_opt[1]:
  #   print("Hard")
  # else:
  #   print("You type a invalid level. Choose a level 'easy' or 'hard' ")