import sys
import math

boost_available = True

# Checkpoints memorises pendant le premier tour.
# Une fois qu'on revient au premier checkpoint, on connait tout le circuit.
checkpoints = []
track_known = False
best_boost_checkpoint = None
last_checkpoint = None

# Positions precedentes pour estimer la vitesse du pod.
last_x = None
last_y = None


def dist2(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

while True:
    x, y, next_checkpoint_x, next_checkpoint_y, next_checkpoint_dist, next_checkpoint_angle = [
        int(i) for i in input().split()
    ]

    opponent_x, opponent_y = [int(i) for i in input().split()]

    checkpoint = (next_checkpoint_x, next_checkpoint_y)

    # Quand le prochain checkpoint change, on l'ajoute a la liste.
    # Si on retombe sur le premier checkpoint, le tour est boucle.
    if checkpoint != last_checkpoint:
        if checkpoint not in checkpoints and not track_known:
            checkpoints.append(checkpoint)
        elif len(checkpoints) > 1 and checkpoint == checkpoints[0]:
            track_known = True

            # Le meilleur BOOST est sur la plus longue portion entre deux checkpoints.
            best_index = 0
            best_distance = 0
            for i in range(len(checkpoints)):
                current_distance = dist2(checkpoints[i - 1], checkpoints[i])
                if current_distance > best_distance:
                    best_distance = current_distance
                    best_index = i
            best_boost_checkpoint = checkpoints[best_index]
        last_checkpoint = checkpoint

    # Estimation simple de la vitesse: position actuelle - position precedente.
    if last_x is None or last_y is None:
        speed_x = 0
        speed_y = 0
    else:
        speed_x = x - last_x
        speed_y = y - last_y

    # On vise un peu "avant" le checkpoint pour compenser la derive du pod.
    # Plus le pod va vite, plus cette correction decale la cible.
    target_x = next_checkpoint_x - speed_x * 3
    target_y = next_checkpoint_y - speed_y * 3

    # Thrust progressif:
    # - angle_factor baisse quand le pod n'est pas aligne avec le checkpoint.
    # - distance_factor baisse quand le pod est proche du checkpoint.
    angle_factor = max(0, 1 - abs(next_checkpoint_angle) / 90)
    distance_factor = min(1, next_checkpoint_dist / 1200)
    thrust = int(100 * angle_factor * distance_factor)

    # BOOST seulement une fois, sur la meilleure ligne droite connue,
    # et seulement si le pod est presque parfaitement aligne.
    if boost_available and track_known and checkpoint == best_boost_checkpoint and next_checkpoint_dist > 5000 and abs(next_checkpoint_angle) < 5:
        thrust = "BOOST"
        boost_available = False

    # SHIELD coute 3 tours d'acceleration.
    # On l'utilise seulement si on poussait deja peu, donc son cout est limite.
    if thrust != "BOOST" and thrust <= 30 and math.hypot(x - opponent_x, y - opponent_y) < 850:
        thrust = "SHIELD"

    last_x = x
    last_y = y

    # Affichage des variables
    print(
        "dist:",
        next_checkpoint_dist,
        "angle:",
        next_checkpoint_angle,
        "track:",
        track_known,
        "best_boost:",
        best_boost_checkpoint,
        "thrust:",
        thrust,
        file=sys.stderr,
        flush=True,
    )
    
    print(int(target_x), int(target_y), thrust)
