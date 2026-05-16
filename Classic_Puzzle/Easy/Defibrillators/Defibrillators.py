import sys
import math

lon = input()
lat = input()
n = int(input())

lon = float(lon.replace(",", "."))
lat = float(lat.replace(",", "."))

min = 0
minaddr = ""
flag = 0

for i in range(n):
    defib = input()
    info = defib.split(";")
    lon1 = float(info[4].replace(",", "."))
    lat1 = float(info[5].replace(",", "."))
    x = (lon1 - lon) * math.cos((lat + lat1) / 2)
    y = (lat1 - lat)
    d = math.sqrt(x*x + y*y) * 6371

    if flag == 0:
        min = d
        minaddr = info[1]
        flag = 1
    elif d < min:
        min = d
        minaddr = info[1]

print(minaddr)