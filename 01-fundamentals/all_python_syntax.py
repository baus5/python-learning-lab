"""
All Python Syntax — Quick Review Notes,

Source:
- "All Python Syntax in 25 Minutes"
- by Beau Carnes
- https://www.youtube.com/watch?v=PNSIWjWAA7o

Added some extra notes.

Tip:
You can try many of these examples directly in the Python shell (>>>)
without using print().
"""

# ==================================================
# Python Basics
# ==================================================

# Basic math
2 + 3 * 6  # 20
(2 + 3) * 6  # 30

# String concatenation
"Alice" + "Bob"  # "AliceBob"
"Alice" "Bob"  # "AliceBob"

# String repetition
"Alice" * 5
# "AliceAliceAliceAliceAlice"

# Variables
message = "Hello"

# Print
print("Hello world!")
print("Hello", message)

# User input
print("What is your name?")
my_name = input()

# f string
print(f"It is good to meet you {my_name}")

# old .format string
print("It is good to meet you {}".format(my_name))

# Length
len("hello")  # 5

# Converts integer to a string
str(29)
# "29"

# Converts deca float into an integer
int(7.7)
# 7

# Type conversion
str(29)  # "29"
int(7.7)  # 7

# ==================================================
# Comparison & Logical Operators
# ==================================================

"""
Comparison Operators

==    Equal to
!=    Not equal to
<     Less than
>     Greater than
<=    Less than or equal to
>=    Greater than or equal to
"""

"hello" == "Hello"  # False
42 == 42.0  # True
"dog" != "cat"  # True

True is True  # True
True is not False  # True

# Logical operators
(4 < 5) and (5 < 6)  # True
(4 < 5) and (9 < 6)  # False

(1 == 2) or (2 == 2)  # True

2 + 2 == 4 and not 2 + 2 == 5 and 2 * 2 == 2 + 2
# True


# ==================================================
# Flow Control
# ==================================================

name = "Alice"

# if statement
if name == "Alice":
    print("Hi, Alice.")

# if / elif / else
if name == "Alice":
    print("Hi, Alice.")
elif name == "Bob":
    print("Hi, Bob.")
else:
    print("Hello, stranger.")


# while loop
spam = 0
while spam < 5:
    print("Hello, world.")
    spam = spam + 1

# break example
while True:
    print("Please type your name.")
    name = input()

    if name == "your name":
        break
print("Thank you!")

# continue example
while True:
    print("Who are you?")
    name = input()

    if name != "Joe":
        continue

    print("Hello, Joe. What is your password? (It is a fish.)")
    password = input()

    if password == "swordfish":
        break
print("Access granted.")


# ==================================================
# for Loops & range()
# ==================================================

for i in range(5):
    print("This is ", i)


for i in range(0, 10, 2):
    print(i)


for i in range(5, -1, -1):
    print(i)


# ==================================================
# for...else
# ==================================================

"""
The else block runs only if the loop finishes
without hitting break.
"""

for i in [1, 2, 3, 4, 5]:
    if i == 3:
        break
else:
    print("Executed only if no break occurs")

"""for...else statement

In Python, a for...else statement is a unique control flow feature where
an else block is attached to a for loop. Unlike its use with if statements,
the else block here executes only if the loop finishes normally
(i.e., it iterates through the entire sequence without being interrupted)

Core Logic

- Loop finishes normally: The else block runs.
- break statement is hit: The else block is skipped.
- Empty sequence: If the loop has nothing to iterate over, the else block runs immediately.

# Common Use Case: Searching,

# This construct is most useful for search operations where you want to perform
# an action if a specific item was not found.

Key Differences from if...else

- In an if...else statement, either the if block or the else block runs—never both.
- In a for...else statement, the else block runs after the for loop completes its
final iteration, provided no break occurred
"""


# Example: Searching for an even number
numbers = [1, 3, 5]

for num in numbers:
    if num % 2 == 0:
        print(f"Found an even number: {num}")
        break  # Skips the else block
else:
    # This runs only if the loop never hits 'break'
    print("No even numbers found.")


# ==================================================
# Modules & Imports
# ==================================================

import random

for i in range(5):
    print(random.randint(1, 10))


# Import everything from a module
from random import *

print(randint(1, 10))


# ==================================================
# System Exit
# ==================================================

import sys

while True:
    print("Type 'exit' to quit.")
    response = input()

    if response == "exit":
        sys.exit()

    print(f"You typed: {response}")
    break


# ==========================================
# Functions Control
# ==========================================


# Simple function
def hello(name):
    print(f"Hello {name}.")


hello("Alice")
hello("Bob")


# ==========================================
# Exception Handling
# ==========================================


# ==========================================
# Lists
# ==========================================


# ==========================================
# Tuples
# ==========================================


# ==========================================
# Dictionaries and Structuring Data
# ==========================================


# ==========================================
# Sets
# ==========================================


# ==========================================
# Comprehensions
# ==========================================


# ==========================================
# Manipulating Strings
# ==========================================


# ==========================================
# String Formatting
# ==========================================


# ==========================================
# Debugging
# ==========================================


# ==========================================
# Lambda Functions
# ==========================================


# ==========================================
# Ternary Conditional Operator
# ==========================================


# ==========================================
# args and kwargs
# ==========================================


# ==========================================
#  _main_ Top-level script environment
# ==========================================
