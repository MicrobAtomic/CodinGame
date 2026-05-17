import sys
import math

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.

    direction_x = ""
    direction_y = ""
    
    if initial_tx > light_x:
        direction_x = "W"
        initial_tx -= 1
    elif initial_tx < light_x:
        direction_x = "E"
        initial_tx += 1
        
    if initial_ty > light_y:
        direction_y = "N"
        initial_ty -= 1
    elif initial_ty < light_y:
        direction_y = "S"
        initial_ty += 1

    print(direction_y + direction_x)
    # A single line providing the move to be made: N NE E SE S SW W or NW
