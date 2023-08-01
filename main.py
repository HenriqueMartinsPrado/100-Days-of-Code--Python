
from art import logo
import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def set_diffilculty():
  level = input("Choose a diffilculty. Type 'easy' or 'hard': ")
  global turns
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

turns = 0
def checK_answer(guess, answer, turns):
  """Check answers againt guess. Returns the number od turns remaining"""
  if guess > answer:
    print("Too high")
    return turns-1
  elif guess < answer:
    print("Too low.")
    return turns-1
  else:
    print(f"You got it. The answer was {answer}")

def game():
  print(logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a the number between 1 and 100.")
  answer = random.randint(1, 100)
  
  turns = set_diffilculty()
  
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    turns = checK_answer(guess, answer, turns)

game()