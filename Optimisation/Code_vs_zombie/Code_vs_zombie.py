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
    danger_immediat = False # Pour savoir si un humain est vraiment menacé

    for h in humains:
        # 1. Trouver le zombie le plus proche de CET humain
        dist_zombie_carre_max = float('inf')
        for z in zombies:
            dist_hz = (h["x"] - z["x"])**2 + (h["y"] - z["y"])**2
            if dist_hz < dist_zombie_carre_max:
                dist_zombie_carre_max = dist_hz
        
        dist_zombie_humain = math.sqrt(dist_zombie_carre_max)
        dist_ash_humain = math.sqrt((ash_x - h["x"])**2 + (ash_y - h["y"])**2)

        # Calcul des tours
        tours_zombie = dist_zombie_humain / 400
        tours_ash = max(0, (dist_ash_humain - 2000)) / 1000

        # Si Ash peut arriver à temps
        if tours_ash <= tours_zombie:
            # On considère qu'un humain est en "danger immédiat" 
            # si un zombie peut l'atteindre en moins de, disons, 6 tours.
            if tours_zombie < 6:
                danger_immediat = True
            
            if dist_ash_humain < distance_min_ash_humain:
                distance_min_ash_humain = dist_ash_humain
                meilleur_humain = h

    # --- APPLICATION DE LA STRATÉGIE ---

    # CAS 1 : Un humain est sauvable ET en danger immédiat -> On va le protéger
    if meilleur_humain is not None and danger_immediat:
        cible_x = meilleur_humain["x"]
        cible_y = meilleur_humain["y"]

    # CAS 2 (Ton idée) : Tout le monde est en sécurité -> On va chercher le zombie le plus proche de Ash
    elif len(zombies) > 0:
        dist_min_zombie = float('inf')
        proche_zombie = zombies[0]
        
        for z in zombies:
            dist_ash_z = (ash_x - z["x"])**2 + (ash_y - z["y"])**2
            if dist_ash_z < dist_min_zombie:
                dist_min_zombie = dist_ash_z
                proche_zombie = z
        
        # On fonce sur le zombie le plus proche pour nettoyer la carte
        cible_x = proche_zombie["x"]
        cible_y = proche_zombie["y"]
        
    # CAS 3 : Plus de zombies, ou situation imprévue -> On reste sur place ou va vers le premier humain
    elif len(humains) > 0:
        cible_x = humains[0]["x"]
        cible_y = humains[0]["y"]

    # Action
    print(f"{cible_x} {cible_y}")