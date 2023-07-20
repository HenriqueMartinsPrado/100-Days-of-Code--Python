# Day 1

# The name of the program to debug is Thonny

# Write your code below this line 👇
print("Hello World!")
print("Hello World!")
print("Hello World!")

print("Hello World!\nHello World!\nHello World!")

print("Henrique"+" Martins")

input("What is your name?")
len(input("What is your name?"))
print(len(input("What is your name?")))

# Project

print("\n=========== Project Day 1 ===========")
city_name = input("What city did you grow up?\n")
pet_name = input("What is the name of your pet?\n")

band = city_name + pet_name

print(band)

# ==================================================================
#  Day 2 

# Data Types

# String

print("Hello"[0])
print("123" + "456")
print("hello" + "world")

# Integer

print(123 + 456)

# To better read the number like 123,456,789, you can user _. The exemplo is goino to be 123_456_789. The python language will interpret that like 123456789

# Float

123.45 

# Boolean 

True 
False

# ==================================================================
# Day 3 

# Conditions

# ex1
# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if (number % 2) == 0:
    print("This is an even number")
else:
    print("This is an odd number.")





# ex2
# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

import math

bmi = math.ceil(weight / (height * height))
#print(f"Your BMI is {bmi}")

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi >= 18.5 and bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi >= 25 and bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi >= 30 and bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")

