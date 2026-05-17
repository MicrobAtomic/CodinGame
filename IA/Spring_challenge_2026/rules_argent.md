# Spring Challenge 2026 - Ligue argent

Les regles de la ligue argent correspondent aux regles completes deja presentes
dans `rules.md`. Je n'ai pas repere de changement mecanique dans la version
francaise fournie.

## Points importants pour notre bot

- La partie dure au maximum 300 tours.
- Score: chaque fruit dans la cabane vaut 1 point, chaque WOOD vaut 4 points,
  IRON ne vaut aucun point.
- Les arbres proches de l'eau poussent beaucoup plus vite.
- Les arbres plantes commencent petits, mais peuvent devenir rentables si on
  les plante assez tot et assez pres de la cabane.
- Un troll peut `PICK` une graine depuis la cabane seulement s'il est adjacent a
  la cabane.
- Un troll peut `PLANT` seulement sur sa case actuelle, s'il transporte un fruit
  du type plante.
- La case de la cabane est le spawn: un `TRAIN` echoue si la case est bloquee.
- Ordre des actions: MOVE, HARVEST, PLANT, CHOP, PICK, TRAIN, DROP, MINE, GROW.

## Strategie argent suivie

- Train uniquement tout debut de partie.
- Construire un verger compact contre la cabane.
- Preferer le cote eau seulement parmi les cases proches de la cabane.
- Replanter le verger pendant la partie pour eviter les voyages lointains en
  fin de game.
- En late game, refuser les arbres trop loin meme s'ils ont des fruits.
