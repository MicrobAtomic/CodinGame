width, height = [int(i) for i in input().split()]
player_x, player_y = [int(i) for i in input().split()]
num_movements = int(input())

world = []
for _ in range(height):
    world.append(list(input()))

for _ in range(num_movements):
    move_x, move_y = [int(j) for j in input().split()]

    world[player_y][player_x] = "_"

    player_x += move_x
    player_y += move_y

    world[player_y][player_x] = "P"

    for line in world:
        print("".join(line))