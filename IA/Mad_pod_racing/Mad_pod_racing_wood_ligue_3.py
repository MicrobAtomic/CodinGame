import sys
import math


while True:
    x, y, next_checkpoint_x, next_checkpoint_y = [int(i) for i in input().split()]

    dx = next_checkpoint_x - x
    dy = next_checkpoint_y - y
    distance = math.sqrt(dx * dx + dy * dy)

    if distance > 6000:
        thrust = 100
    elif distance > 1500:
        thrust = 60
    else:
        thrust = 30

    print("distance:", int(distance), "thrust:", thrust, file=sys.stderr, flush=True)
    print(next_checkpoint_x, next_checkpoint_y, thrust)
