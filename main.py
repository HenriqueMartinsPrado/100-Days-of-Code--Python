
from art import logo
import random

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a the number between 1 and 100.")
guess = int(input("Make a guess: "))
answer = random.randint(1, 100)

# level_opt = {"easy": 5, "hard": 10}
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# is_gameover = False

def set_diffilculty():
  level = input("Choose a diffilculty. Type 'easy' or 'hard': ")
  if level == "easy":
    turns = EASY_LEVEL_TURNS
  else:
    turns = HARD_LEVEL_TURNS


def checK_answer(guess, answer):
  if guess > answer:
    print("Too high")
  elif guess < answer:
    print("Too low.")
  else:
    print(f"You got it. The answer was {answer}")