import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x, y = [int(i) for i in input().split()]

# game loop
x_min = 0
x_max = w - 1
y_min = 0
y_max = h - 1
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)

    if "U" in bomb_dir:
        y_max = y - 1
    elif "D" in bomb_dir:
        y_min = y + 1
    if "R" in bomb_dir:
        x_min = x + 1
    elif "L" in bomb_dir:
        x_max = x - 1

    x = (x_min + x_max) // 2
    y = (y_min + y_max) // 2

    # the location of the next window Batman should jump to.
    print(x, y)
