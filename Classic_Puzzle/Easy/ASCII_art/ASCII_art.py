import sys
import math
import re

l = int(input())
h = int(input())
t = input().lower()
for i in range(h):
    row = input()
    blocs = re.findall('.' * l, row)
    alphabet = "abcdefghijklmnopqrstuvwxyz?"
    letter_dict = dict(zip(alphabet, blocs))
    for char in t:
        if char in letter_dict:
            print(letter_dict[char], end="")
        else: 
            print(letter_dict['?'], end="")
    print()
