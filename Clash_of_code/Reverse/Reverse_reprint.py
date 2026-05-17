import sys
import math

w1, h1 = [int(i) for i in input().split()]
w2, h2 = [int(i) for i in input().split()]
grid = [input() for _ in range(h1)]

for y in range(h1):
    for x in range(w1):
        if y % (h2 + 1) == 0 or x % (w2 + 1) == 0:
            print(".", end="")
        else:
            count = {}

            for yy in range(y % (h2 + 1), h1, h2 + 1):
                for xx in range(x % (w2 + 1), w1, w2 + 1):
                    char = grid[yy][xx]
                    if char != ".":
                        if char not in count:
                            count[char] = 0
                        count[char] += 1

            best_char = "."
            best_count = 0
            for char in count:
                if count[char] > best_count:
                    best_char = char
                    best_count = count[char]

            print(best_char, end="")
    print()
