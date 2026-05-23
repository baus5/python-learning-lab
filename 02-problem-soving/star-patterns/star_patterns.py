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
""" Instead of writing code first, always think:
for each row:
    print spaces
    print stars
    move to next line
"""

"""My thoughts,

At each step we decrease and expand — we decrease spaces and increase stars.
In the code context, we work with lines. So each line, for example,
includes an even number of spaces and an odd number of stars.
Basically, line by line, this creates asymmetry. (Maybe except last line)

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


# ------------------------------------------------------------------------------
# 5. Diamond Pattern
# ------------------------------------------------------------------------------
""" Instead of writing code first, always think:
for each row:
    print spaces
    print stars
    move to next line
"""

pattern_title("Diamond Pattern")

rows = 7
upper_rows = 7 // 2 + 1
lower_rows = 7 // 2

# upper part
for i in range(upper_rows):
    # spaces
    for j in range((upper_rows - i) - 1):
        print(" ", end=" ")

    # stars
    for k in range(i * 2 + 1):
        print("*", end=" ")

    print()


# for i in range(rows // 2 + 1):
#     # spaces
#     for j in range(((rows // 2 + 1) - i) - 1):
#         print(" ", end=" ")

#     # stars
#     for k in range(i * 2 + 1):
#         print("*", end=" ")
#     print()


# lower part
for i in range(lower_rows):

    # spaces
    # range = 1 2 3
    for j in range(i + 1):
        print(" ", end=" ")

    # stars
    for k in range((lower_rows - i) * 2 - 1):
        print("*", end=" ")

    print()


"""
   *
  ***
 *****
*******
 *****
  ***
   *
"""


"""
my logic steps:
i am starting thinking with stars

--------------------------------------------------------------------------------
for stars = 1 3 5 7...

simple math for create any odd numbers:
2x + 1

this is why we use:
i * 2 + 1 (odd number formula)


for stars each i:
0 * 2 + 1 = 1 star
1 * 2 + 1 = 3 star
2 * 2 + 1 = 5 star
3 * 2 + 1 = 7 star (last line for upper part)

this is range(4)

--------------------------------------------------------------------------------
(this block will come before the star block)
for spaces = 3 2 1 0

we gonna use decrease formula:
x - 1 

(use dots instead of spaces better understanding or dont confuse 
about print(, end=" ") just change it end="")
think each end with space like grids.

for spaces(or dots) each i:
4 - 1 = 3 space
3 - 1 = 2 space
2 - 1 = 1 space
1 - 1 = 0 space (last line for upper part)

so this is range(4, 0, -1):
"""

# for i in range(rows // 2 + 1):
#     # spaces
#     for j in range(((rows // 2 + 1) - i) - 1):
#         print(" ", end=" ")

#     # stars
#     for k in range(i * 2 + 1):
#         print("*", end=" ")
#     print()


# lower part
"""my logic:

so we already printed upper part. lower part is same logic but reversed order:

im gonna start with spaces this time:

1 - 1 = 0 space (last line for upper part)
for spaces(or dots) each i:
2 - 1 = 1 space
3 - 1 = 2 space
4 - 1 = 3 space

this is range(1, 4)


3 * 2 + 1 = 7 star (remained line from upper part)
for stars each i:
2 * 2 + 1 = 5 star
1 * 2 + 1 = 3 star
0 * 2 + 1 = 1 star

this is range(2, 0, -1)

"""
# 3.5 = 0 1 2 = i
# for i in range(rows // 2):

#     # spaces
#     # range = 1 2 3
#     for j in range(i + 1):
#         print(" ", end=" ")

#     # stars
#     for k in range((rows // 2 - i) * 2 - 1):
#         print("*", end=" ")

#     print()
