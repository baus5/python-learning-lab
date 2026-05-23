"""Star Patterns Practice by baus5,

This file contains beginner pattern problems using Python loops.

All patterns are implemented for learning and problem-solving practice.
Some are guided by tutorials or references, while others are solved independently
to strengthen problem-solving skills.

Main concepts:
- range() function
- nested loops
- terminal output formatting
"""

# range() function notes
"""
range() function

Creates a sequence of integers.

Syntax:
- range(stop) -> 0 to stop-1
- range(start, stop) -> start to stop-1
- range(start, stop, step) -> custom step size

Examples:
- range(4) → 0, 1, 2, 3
- range(i, j) produces i, i+1, i+2, ..., j-1.
"""


# Terminal Output setting for better visualize
def pattern_title(title):
    """Displays a formatted section title for terminal readability."""
    print("", title, "-" * len(title), sep="\n")
    # print(f"\n{title}\n" + "-" * len(title))


# ------------------------------------------------------------------------------
# 01 Simple Square Pattern
# ------------------------------------------------------------------------------
pattern_title("Simple Square Pattern")

rows = 4

for i in range(rows):
    for j in range(rows):
        print("*", end=" ")
    print()


# ------------------------------------------------------------------------------
# 02 Right Triangle Pattern
# ------------------------------------------------------------------------------
pattern_title("Right Triangle Pattern")

rows = 4

for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()


# ------------------------------------------------------------------------------
# 03 Inverted Triangle
# ------------------------------------------------------------------------------
pattern_title("Inverted Triangle")

rows = 4

for i in range(rows, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()


# ------------------------------------------------------------------------------
# 04 Pyramid Pattern
# ------------------------------------------------------------------------------
"""
What this code is trying to print

      *
    * * *
  * * * * *
* * * * * * *
"""

"""My thoughts,

At each step we decrease and expand — we decrease spaces and increase stars.
In the code context, we work with lines. So each line, for example,
includes an even number of spaces and an odd number of stars.
Basically, line by line, this creates asymmetry.

But in conclusion, we create a shape, and this shape has symmetry,
so we are essentially creating symmetry from asymmetry.
"""


"""
Pyramid patterns:
step-by-step construction of a symmetric shape using
shifting offsets and odd-width growth
"""


"""
PYRAMID PATTERN - CORE IDEA

A pyramid is built row by row using two controlled changes:

1. LEFT SPACES (alignment control)
   - Starts high and decreases each row
   - Pushes the stars toward the center

2. STARS (shape growth)
   - Starts small and increases each row
   - Always grows in an odd pattern (1, 3, 5, 7...)

FORMULAS:
- spaces = rows - i - 1
- stars  = 2 * i + 1

BIG IDEA:
Each row = controlled shift (spaces) + controlled growth (stars)

This combination creates a centered geometric shape (triangle).
"""


""" Instead of writing code first, always think:
for each row:
    print spaces
    print stars
    move to next line
"""

pattern_title("Pyramid Pattern")

rows = 4

for i in range(rows):
    # spaces
    for j in range(rows - i - 1):
        print(" ", end=" ")

    # stars
    for k in range(2 * i + 1):
        print("*", end=" ")

    print()
