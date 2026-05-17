import sys


# The game is a hidden Pac-Man:
# input 1..4 are the free/wall flags around Pac-Man,
# the last coordinate pair is Pac-Man, previous pairs are ghosts.
COMMAND = {
    "right": "A",
    "down": "C",
    "up": "D",
    "left": "E",
}

REVERSE = {
    "right": "left",
    "left": "right",
    "up": "down",
    "down": "up",
}

# In this challenge Y grows upward, so "down" is y - 1.
DELTA = {
    "right": (1, 0),
    "down": (0, -1),
    "up": (0, 1),
    "left": (-1, 0),
}


def read_int():
    try:
        return int(input())
    except EOFError:
        sys.exit(0)


width = read_int()
height = read_int()
player_count = read_int()

visited = set()
last_pos = None
last_dir = None

while True:
    try:
        first_input = input().strip()
        second_input = input().strip()
        third_input = input().strip()
        fourth_input = input().strip()
    except EOFError:
        break

    positions = []
    for _ in range(player_count):
        x, y = [int(value) for value in input().split()]
        positions.append((x, y))

    ghosts = positions[:-1]
    pacman = positions[-1]

    if last_pos is not None and last_dir is not None and pacman != last_pos:
        dx = pacman[0] - last_pos[0]
        dy = pacman[1] - last_pos[1]
        DELTA[last_dir] = (dx, dy)
        opposite = REVERSE[last_dir]
        DELTA[opposite] = (-dx, -dy)

    visited.add(pacman)

    open_direction = {
        "down": first_input == "_",
        "right": second_input == "_",
        "up": third_input == "_",
        "left": fourth_input == "_",
    }

    ghost_cells = set(ghosts)
    candidates = []

    for direction, is_open in open_direction.items():
        if not is_open:
            continue

        dx, dy = DELTA[direction]
        next_pos = (pacman[0] + dx, pacman[1] + dy)
        ghost_distance = min(
            abs(next_pos[0] - ghost_x) + abs(next_pos[1] - ghost_y)
            for ghost_x, ghost_y in ghosts
        )

        score = 0
        if next_pos not in visited:
            score += 100
        score += ghost_distance * 8

        if next_pos in ghost_cells:
            score -= 10_000
        if ghost_distance <= 1:
            score -= 500
        if last_dir is not None and direction == REVERSE[last_dir]:
            score -= 25

        candidates.append((score, direction))

    if candidates:
        _, chosen_dir = max(candidates)
        answer = COMMAND[chosen_dir]
        last_dir = chosen_dir
    else:
        answer = "B"
        last_dir = None

    last_pos = pacman
    print(answer)
