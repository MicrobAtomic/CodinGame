import sys
import math

# Save humans, destroy zombies!


# game loop
while True:
    # 1. POSITION DE ASH
    ash_x, ash_y = [int(i) for i in input().split()]
    
    # 2. LECTURE DES HUMAINS
    human_count = int(input())
    humains = []
    for i in range(human_count):
        h_id, h_x, h_y = [int(j) for j in input().split()]
        humains.append({"id": h_id, "x": h_x, "y": h_y})

    # 3. LECTURE DES ZOMBIES
    zombie_count = int(input())
    zombies = []
    for i in range(zombie_count):
        z_id, z_x, z_y, z_xn, z_yn = [int(j) for j in input().split()]
        zombies.append({"id": z_id, "x": z_x, "y": z_y, "next_x": z_xn, "next_y": z_yn})

    # --- PHASE DE RÉFLEXION ---
    
    cible_x = ash_x
    cible_y = ash_y
    meilleur_humain = None
    distance_min_ash_humain = float('inf')

    for h in humains:
        # 1. Trouver le zombie le plus proche de CET humain
        dist_zombie_carre_max = float('inf')
        for z in zombies:
            dist_hz = (h["x"] - z["x"])**2 + (h["y"] - z["y"])**2
            if dist_hz < dist_zombie_carre_max:
                dist_zombie_carre_max = dist_hz
        
        # On calcule les vraies distances (avec racine carrée) pour estimer les tours
        dist_zombie_humain = math.sqrt(dist_zombie_carre_max)
        dist_ash_humain = math.sqrt((ash_x - h["x"])**2 + (ash_y - h["y"])**2)

        # 2. Calculer le nombre de tours approximatifs avant l'impact
        # Le zombie avance de 400 par tour
        tours_zombie = dist_zombie_humain / 400
        
        # Ash avance de 1000 par tour, et tire à 2000 de distance.
        # Donc la distance effective à parcourir est (dist_ash_humain - 2000)
        tours_ash = max(0, (dist_ash_humain - 2000)) / 1000

        # 3. SI ASH PEUT ARRIVER À TEMPS (ou en même temps)
        if tours_ash <= tours_zombie:
            # Parmi les humains sauvables, on choisit celui le plus proche de Ash
            # (C'est la stratégie la plus sûre pour en garder au moins un en vie)
            if dist_ash_humain < distance_min_ash_humain:
                distance_min_ash_humain = dist_ash_humain
                meilleur_humain = h

    # 4. Assigner la cible
    if meilleur_humain is not None:
        cible_x = meilleur_humain["x"]
        cible_y = meilleur_humain["y"]
    else:
        # Si aucun humain n'est sauvable (scénario catastrophe), 
        # on fonce quand même sur le premier humain de la liste par défaut
        if len(humains) > 0:
            cible_x = humains[0]["x"]
            cible_y = humains[0]["y"]

    # Action
    print(f"{cible_x} {cible_y}")