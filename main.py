
from art import logo
import random

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a the number between 1 and 100.")
answer = random.randint(1, 100)

# level_opt = {"easy": 5, "hard": 10}
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# is_gameover = False

def set_diffilculty():
  level = input("Choose a diffilculty. Type 'easy' or 'hard': ")
  global turns
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def checK_answer(guess, answer):
  if guess > answer:
    print("Too high")
  elif guess < answer:
    print("Too low.")
  else:
    print(f"You got it. The answer was {answer}")

guess = int(input("Make a guess: "))
turns = 0
print(f"You have {} attempts remaining to guess the number.")