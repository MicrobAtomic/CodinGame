import sys

# nb_floors: number of floors
# width: width of the area
# nb_rounds: maximum number of rounds
# exit_floor: floor on which the exit is found
# exit_pos: position of the exit on its floor
# nb_total_clones: number of generated clones
# nb_additional_elevators: ignore (always zero)
# nb_elevators: number of elevators
nb_floors, width, nb_rounds, exit_floor, exit_pos, nb_total_clones, nb_additional_elevators, nb_elevators = [
    int(i) for i in input().split()
]

elevators = {}
for _ in range(nb_elevators):
    # elevator_floor: floor on which this elevator is found
    # elevator_pos: position of the elevator on its floor
    elevator_floor, elevator_pos = [int(j) for j in input().split()]
    elevators[elevator_floor] = elevator_pos

# Sur chaque etage, la cible est:
# - l'ascenseur si ce n'est pas l'etage de sortie
# - la sortie si c'est l'etage final
targets = {}
for floor, pos in elevators.items():
    targets[floor] = pos
targets[exit_floor] = exit_pos

while True:
    inputs = input().split()
    clone_floor = int(inputs[0])  # floor of the leading clone
    clone_pos = int(inputs[1])  # position of the leading clone on its floor
    direction = inputs[2]  # direction of the leading clone: LEFT or RIGHT

    if clone_floor == -1:
        print("WAIT")
        continue

    target_pos = targets[clone_floor]

    going_left_but_target_is_right = direction == "LEFT" and clone_pos < target_pos
    going_right_but_target_is_left = direction == "RIGHT" and clone_pos > target_pos

    if going_left_but_target_is_right or going_right_but_target_is_left:
        print("BLOCK")
    else:
        print("WAIT")
