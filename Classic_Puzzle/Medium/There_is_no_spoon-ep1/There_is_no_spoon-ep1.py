import sys
import math

# Don't let the machines win. You are humanity's last hope...

width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis

grid = []
for i in range(height):
    line = input()  # width characters, each either 0 or .
    grid.append(line)

for y in range(height):
    for x in range(width):
        if grid[y][x] == '0':
            rx, ry = -1, -1
            bx, by = -1, -1

            for next_x in range(x + 1, width):
                if grid[y][next_x] == '0':
                    rx = next_x
                    ry = y
                    break

            for next_y in range(y + 1, height):
                if grid[next_y][x] == '0':
                    bx = x
                    by = next_y
                    break

            print(f"{x} {y} {rx} {ry} {bx} {by}")
