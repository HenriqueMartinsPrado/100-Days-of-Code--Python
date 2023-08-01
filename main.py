
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

def checK_answer(guess, answer):
  if guess > answer:
    print("Too high")
  elif guess < answer:
    print("Too low.")
  else:
    print(f"You got it. The answer was {answer}")

def game():
  print(logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a the number between 1 and 100.")
  answer = random.randint(1, 100)
  
  turns = set_diffilculty()
  print(f"You have {turns} attempts remaining to guess the number.")
  
  guess = 0
  while guess != answer:
    guess = int(input("Make a guess: "))
    checK_answer(guess, answer)