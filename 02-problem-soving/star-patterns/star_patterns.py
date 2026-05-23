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

ROWS = 4

for i in range(ROWS):
    for j in range(ROWS):
        print("*", end=" ")
    print()


# ------------------------------------------------------------------------------
# 02 Right Triangle Pattern
# ------------------------------------------------------------------------------
pattern_title("Right Triangle Pattern")

ROWS = 4

for i in range(1, ROWS + 1):
    for j in range(i):
        print("*", end=" ")
    print()


# ------------------------------------------------------------------------------
# 03 Inverted Triangle
# ------------------------------------------------------------------------------
pattern_title("Inverted Triangle")

ROWS = 4

for i in range(ROWS, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()


# ------------------------------------------------------------------------------
# 04 Pyramid Pattern
# ------------------------------------------------------------------------------
pattern_title("Pyramid Pattern")

ROWS = 7
