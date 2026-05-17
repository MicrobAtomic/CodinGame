import sys
import math


FRICTION = 0.85
POD_RADIUS = 400
CHECKPOINT_RADIUS = 600


laps = int(input())
checkpoint_count = int(input())
checkpoints = []

for _ in range(checkpoint_count):
    checkpoint_x, checkpoint_y = [int(i) for i in input().split()]
    checkpoints.append((checkpoint_x, checkpoint_y))


def distance(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])


def dist2(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def sub(a, b):
    return a[0] - b[0], a[1] - b[1]


def mul(a, value):
    return a[0] * value, a[1] * value


def angle_degrees(vector):
    angle = math.degrees(math.atan2(vector[1], vector[0]))
    if angle < 0:
        angle += 360
    return angle


def angle_diff(a, b):
    diff = b - a
    if diff < 0:
        diff += 360
    if diff > 180:
        return 360 - diff
    return diff


def current_checkpoint(pod):
    return checkpoints[pod["checkpoint_id"]]


def next_checkpoint(pod):
    return checkpoints[(pod["checkpoint_id"] + 1) % checkpoint_count]


def closest_point_to_line(a, b, p):
    a_to_p = sub(p, a)
    a_to_b = sub(b, a)
    line_length2 = dist2(a, b)

    if line_length2 == 0:
        return p

    dot = a_to_p[0] * a_to_b[0] + a_to_p[1] * a_to_b[1]
    t = dot / line_length2
    return a[0] + a_to_b[0] * t, a[1] + a_to_b[1] * t


def degrees_to_checkpoint(pod, checkpoint):
    pod_pos = (pod["x"], pod["y"])
    wanted_angle = angle_degrees(sub(checkpoint, pod_pos))
    return angle_diff(pod["angle"], wanted_angle)


def is_going_to_enter_checkpoint_soon(pod):
    checkpoint = current_checkpoint(pod)
    pos = (pod["x"], pod["y"])
    velocity = (pod["vx"], pod["vy"])

    for _ in range(6):
        velocity = mul(velocity, FRICTION)
        pos = add(pos, velocity)

        if distance(pos, checkpoint) <= CHECKPOINT_RADIUS:
            return True

    return False


def is_going_to_collide(pod, other):
    pod_next = (pod["x"] + pod["vx"] * FRICTION, pod["y"] + pod["vy"] * FRICTION)
    other_next = (other["x"] + other["vx"] * FRICTION, other["y"] + other["vy"] * FRICTION)
    return distance(pod_next, other_next) <= POD_RADIUS * 2


def collision_score(pod, other):
    if not is_going_to_collide(pod, other):
        return 0

    checkpoint = current_checkpoint(pod)
    pos = (pod["x"], pod["y"])
    base_distance = distance(pos, checkpoint)

    pod_delta = (pod["vx"] * FRICTION, pod["vy"] * FRICTION)
    other_delta = (other["vx"] * FRICTION * 10, other["vy"] * FRICTION * 10)
    estimated_after_collision = add(add(pos, pod_delta), other_delta)

    return base_distance - distance(estimated_after_collision, checkpoint)


def should_shield(pod_index, pods):
    if shield_cooldown[pod_index] > 0:
        return False

    pod = pods[pod_index]
    ally = pods[1 - pod_index]

    ally_score = collision_score(ally, pod)

    # Le pod 2 peut parfois se mettre en bouclier pour pousser le pod 1.
    if pod_index == 1 and ally_score > 10:
        return True

    # Si on risque de gener notre autre pod, on garde le bouclier eteint.
    if ally_score < -10:
        return False

    my_score_with_ally = collision_score(pod, ally)
    if my_score_with_ally > 10:
        return False

    for enemy in pods[2:]:
        enemy_score = collision_score(enemy, pod)
        my_score = collision_score(pod, enemy)

        # Si l'ennemi sortirait perdant de la collision, on devient lourd.
        if enemy_score < -10:
            return True

        # Si la collision nous aide, autant rester leger.
        if my_score > 10:
            return False

        # Si elle nous penalise, bouclier.
        if my_score < -10:
            return True

    return False


def race_action(pod_index, pods):
    global boost_available

    pod = pods[pod_index]
    checkpoint = current_checkpoint(pod)
    pod_pos = (pod["x"], pod["y"])
    velocity = (pod["vx"], pod["vy"])

    target = checkpoint
    degrees = degrees_to_checkpoint(pod, checkpoint)
    finished_soon = passed_checkpoints[pod_index] >= checkpoint_count * laps - 1

    previous_delta = mul(velocity, FRICTION)
    future_pos = add(pod_pos, previous_delta)
    previous_speed = distance((0, 0), previous_delta)

    if not finished_soon and is_going_to_enter_checkpoint_soon(pod):
        target = next_checkpoint(pod)
        degrees = degrees_to_checkpoint(pod, target)
    elif previous_speed > 50 and degrees < 70 and distance(future_pos, checkpoint) < distance(pod_pos, checkpoint):
        line_point = closest_point_to_line(pod_pos, checkpoint, future_pos)
        target = add(line_point, sub(line_point, future_pos))

    if degrees < 90:
        thrust = math.ceil(100 * math.cos(degrees / 180))
    else:
        thrust = 0

    if boost_available:
        boost_wait[pod_index] -= 1
        if (pod_index == 0 and turn == 0) or (
            boost_wait[pod_index] < 0
            and degrees < 5
            and distance(pod_pos, checkpoint) > longest_stretch_candidate
        ):
            boost_available = False
            return int(target[0]), int(target[1]), "BOOST"

    if should_shield(pod_index, pods):
        shield_cooldown[pod_index] = 4
        return int(target[0]), int(target[1]), "SHIELD"

    return int(target[0]), int(target[1]), thrust


longest_stretch_candidate = 0
for i in range(checkpoint_count):
    current_distance = distance(checkpoints[i], checkpoints[(i + 1) % checkpoint_count])
    if current_distance > longest_stretch_candidate:
        longest_stretch_candidate = current_distance

longest_stretch_candidate *= 0.70

boost_available = True
boost_wait = [30, 30]
last_checkpoint_ids = [None, None, None, None]
passed_checkpoints = [0, 0, 0, 0]
shield_cooldown = [0, 0]
turn = 0

while True:
    pods = []

    for _ in range(4):
        x, y, vx, vy, angle, next_checkpoint_id = [int(i) for i in input().split()]
        pods.append(
            {
                "x": x,
                "y": y,
                "vx": vx,
                "vy": vy,
                "angle": angle,
                "checkpoint_id": next_checkpoint_id,
            }
        )

    for i in range(4):
        if last_checkpoint_ids[i] is not None and pods[i]["checkpoint_id"] != last_checkpoint_ids[i]:
            passed_checkpoints[i] += 1
        last_checkpoint_ids[i] = pods[i]["checkpoint_id"]

    for i in range(2):
        if shield_cooldown[i] > 0:
            shield_cooldown[i] -= 1

    actions = [race_action(0, pods), race_action(1, pods)]

    print(
        "turn:",
        turn,
        "passed:",
        passed_checkpoints,
        file=sys.stderr,
        flush=True,
    )

    for target_x, target_y, thrust in actions:
        print(target_x, target_y, thrust)

    turn += 1
