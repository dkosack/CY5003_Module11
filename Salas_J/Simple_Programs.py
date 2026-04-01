# Simple_Programs.py

print("\n=======================================")
print(" MODULE 1 MINI PROJECTS")
print("=======================================\n")

print("In this section, you'll create simple programs using what you've learned so far!\n")
print("Let's get started with a few mini projects.\n")
# ---------------------------
# Project 1: Hello, Name!
# ---------------------------

print("\nPROJECT 1: Hello, Name!")
name = input("Enter your name: ")
print("Hello,", name, "! Welcome to CyberVets Python.\n")

# ---------------------------
# Project 2: Basic Calculator
# ---------------------------

print("PROJECT 2: Small Calculator")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print()

# ---------------------------
# Project 3: Motivational Quote Generator
# ---------------------------

print("PROJECT 3: Motivational Quote")

import random

quotes = [
    "Keep going—you’re doing great!",
    "Every day is progress.",
    "Small steps lead to big results.",
    "You’re learning a valuable skill!",
    "Believe in yourself!"
]

print("Your quote of the day:")
print(random.choice(quotes))

print("\nGREAT JOB! You've completed Module 1.")
print("Feel free to revisit any lesson or try the projects again!")
