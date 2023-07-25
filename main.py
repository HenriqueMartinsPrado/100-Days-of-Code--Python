# ==================================================================
# Day 8

# name = input("What is your name? ")

# def my_function(name):
#  print(f"Hello {name}")

# my_function(name)

# ========

name = input("What is your name? ")
location = input("What are you right now? ")

def greet(name, location):
  print(f"Hi {name}")
  print(f"We added your location {location} in our databases")

greet(location=location, name=name)