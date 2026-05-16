import sys
import math

message = input()

add = ""
for letter in message:
    binaire = f"{ord(letter):07b}"
    add = add + binaire

l = 0
while l < len(add):
    count = 1
    while l + 1 < len(add) and add[l] == add[l + 1]:
        count += 1
        l += 1
    if (add[l] == '1'):
        start_bloc = '0'
    else:
        start_bloc = "00"
    if l + 1 < len(add):
        print(start_bloc, "0" * count, end=" ")
    else:
        print(start_bloc, "0" * count, end="")
    l += 1