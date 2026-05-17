import sys
import math

ld_x_gauche = 0
ld_y_gauche = 0

ld_x_droite = 0
ld_y_droite = 0

land_x = 0
land_y = 0
flag = 0

last_land_x = 0
last_land_y = 0

surface_n = int(input())  # the number of points used to draw the surface of Mars.
for i in range(surface_n):
    # land_x: X coordinate of a surface point. (0 to 6999)
    # land_y: Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
    land_x, land_y = [int(j) for j in input().split()]

    if i > 0 and flag == 0 and land_y == last_land_y:
        ld_x_gauche = last_land_x
        ld_y_gauche = last_land_y
        ld_x_droite = land_x
        ld_y_droite = land_y
        flag = 1

    last_land_x = land_x
    last_land_y = land_y

# Marge d'erreur
marge_erreur = 150
ld_x_gauche_reel = ld_x_gauche
ld_x_droite_reel = ld_x_droite
ld_x_gauche += marge_erreur
ld_x_droite -= marge_erreur

first_turn = True
low_fuel_landing = False

# game loop
while True:
    # h_speed: the horizontal speed (in m/s), can be negative.
    # v_speed: the vertical speed (in m/s), can be negative.
    # fuel: the quantity of remaining fuel in liters.
    # rotate: the rotation angle in degrees (-90 to 90).
    # power: the thrust power (0 to 4).
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]

    if first_turn:
        low_fuel_landing = fuel <= 600 and y > 2500 and x < ld_x_gauche_reel
        first_turn = False

    print("ld_y_gauche: ", ld_y_gauche, "ld_y_droite: ", ld_y_droite, file=sys.stderr, flush=True)
    print("ld_x_gauche: ", ld_x_gauche, "ld_x_droite: ", ld_x_droite, file=sys.stderr, flush=True)

    altitude = y - ld_y_gauche
    in_safe_zone = ld_x_gauche <= x <= ld_x_droite
    in_real_zone = ld_x_gauche_reel <= x <= ld_x_droite_reel

    if not in_safe_zone and not (altitude < 600 and in_real_zone and abs(h_speed) <= 20):
        # Phase 1: aller vers la zone d'atterrissage.
        print("go to landing zone", file=sys.stderr, flush=True)

        if x < ld_x_gauche:
            distance = ld_x_gauche - x
            rotate = -min(20, max(0, distance // 3))
        elif x > ld_x_droite:
            distance = x - ld_x_droite
            rotate = min(20, max(0, distance // 3))

        # Si on va deja trop vite horizontalement, on freine un peu.
        if h_speed > 42:
            rotate = 30
        elif h_speed < -42:
            rotate = -30

        if low_fuel_landing:
            if v_speed < -35:
                power = 4
            elif v_speed < -25:
                power = 3
            else:
                power = 2
        elif v_speed < -2:
            power = 4
        else:
            power = 3

    else:
        # Phase 2: on est au-dessus de la zone, on stabilise l'horizontal.
        print("stabilisation / landing", file=sys.stderr, flush=True)

        if altitude < 500 and abs(h_speed) <= 20:
            rotate = 0
            power = 4
        elif h_speed > 10:
            rotate = 30
            power = 4
        elif h_speed < -10:
            rotate = -30
            power = 4
        else:
            rotate = 0

            # Phase 3: landing vertical.
            if low_fuel_landing:
                if abs(v_speed) > 38:
                    power = 4
                elif abs(v_speed) > 30:
                    power = 3
                else:
                    power = 2
            elif abs(v_speed) > 25:
                power = 4
            else:
                power = 3

    # 2 integers: rotate power. rotate is the desired rotation angle (should be 0 for level 1), power is the desired thrust power (0 to 4).
    print(int(rotate), power)
