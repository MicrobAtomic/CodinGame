import sys
import math

min = 5526
keep = 5526
n = int(input())  # the number of temperatures to analyse

if n == 0:
    print(0)
else:
    for i in input().split():
        # t: a temperature expressed as an integer ranging from -273 to 5526
        t = int(i)
        abs_t = abs(t)
        if abs_t < min:
            min = abs_t
            keep = t
        elif abs_t == min and keep < t:
                keep = t
    print(keep)