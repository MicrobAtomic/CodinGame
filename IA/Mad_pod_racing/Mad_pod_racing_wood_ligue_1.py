import sys
import math


boost_available = True

while True:
    x, y, next_checkpoint_x, next_checkpoint_y, next_checkpoint_dist, next_checkpoint_angle = [
        int(i) for i in input().split()
    ]
    opponent_x, opponent_y = [int(i) for i in input().split()]

    if next_checkpoint_angle > 90 or next_checkpoint_angle < -90:
        thrust = 0
    elif boost_available and next_checkpoint_dist > 5000 and abs(next_checkpoint_angle) < 5:
        thrust = "BOOST"
        boost_available = False
    else:
        thrust = 100

    print(
        "dist:",
        next_checkpoint_dist,
        "angle:",
        next_checkpoint_angle,
        "thrust:",
        thrust,
        file=sys.stderr,
        flush=True,
    )
    print(next_checkpoint_x, next_checkpoint_y, thrust)
