
from art import logo
import random

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a the number between 1 and 100.")
level = input("Choose a diffilculty. Type 'easy' or 'hard': ")
guess = int(input("Make a guess: "))

answer = random.randint(1, 100)

level_opt = {"easy": 5, "hard": 10}
is_gameover = False


def checK_answer(guess, answer):
  if guess > answer:
    print("Too high")
  elif guess < answer:
    pritn("Too low.")
  else:
    print("You got it. The answer was {answer}")