import sys
import math

tab = []
n = int(input())
for i in range(n):
    pi = int(input())
    tab.append(pi)

tab.sort()

min_diff = tab[1] - tab[0]

for i in range(1, n - 1):
    dif = tab[i+1] - tab[i]
    if dif < min_diff:
        min_diff = dif
        
print(min_diff)