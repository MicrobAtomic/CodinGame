I=input;S=lambda:I().split();a=S();d=dict(S()for _ in[0]*int(a[7]));d[a[3]]=a[4]
while 1:f,x,s=S();print(eval(x+'<>'[s>'M']+d.get(f,x))*'BLOCK'or'WAIT')

# Version lisible des idees utilisees au-dessus:
#
# I=input
# On donne un nom plus court a input pour gagner des caracteres.
#
# S=lambda:I().split()
# S() lit une ligne et la decoupe directement en morceaux.
# Exemple: "2 10 RIGHT" devient ["2", "10", "RIGHT"].
#
# a=S()
# Lit la ligne d'initialisation:
# nbFloors width nbRounds exitFloor exitPos nbTotalClones nbAdditionalElevators nbElevators
#
# d=dict(S()for _ in[0]*int(a[7]))
# Lit toutes les lignes d'ascenseurs et cree un dictionnaire:
# cle = etage, valeur = position de l'ascenseur.
# Exemple: si un ascenseur est "3 12", alors d["3"] = "12".
# [0]*int(a[7]) sert juste a repeter la lecture nbElevators fois.
#
# d[a[3]]=a[4]
# Ajoute aussi la sortie comme cible:
# a[3] = exitFloor, a[4] = exitPos.
# Donc sur l'etage final, la cible n'est pas un ascenseur mais la sortie.
#
# while 1:
# Boucle infinie du jeu CodinGame.
#
# f,x,s=S()
# Lit le clone de tete:
# f = etage du clone, x = position du clone, s = direction.
#
# d.get(f,x)
# Donne la cible de l'etage f.
# Si f vaut "-1", donc aucun clone actif, l'etage n'existe pas dans d.
# Dans ce cas d.get(f,x) renvoie x, ce qui force une comparaison fausse.
#
# s>'M'
# Sert a distinguer LEFT et RIGHT avec peu de caracteres.
# "RIGHT" > "M" donne True.
# "LEFT" > "M" donne False.
#
# '<>'[s>'M']
# Si s est LEFT, s>'M' vaut False donc index 0: on prend "<".
# Si s est RIGHT, s>'M' vaut True donc index 1: on prend ">".
#
# x+'<>'[s>'M']+d.get(f,x)
# Fabrique une comparaison sous forme de texte.
# Si le clone va a droite, ca peut donner "10>5".
# Si le clone va a gauche, ca peut donner "3<8".
#
# eval(...)
# Execute cette comparaison et renvoie True ou False.
# True veut dire: le clone s'eloigne de sa cible, donc il faut BLOCK.
# False veut dire: il va dans le bon sens, donc WAIT.
#
# eval(...)*'BLOCK'or'WAIT'
# Si eval vaut True, True*'BLOCK' donne "BLOCK".
# Si eval vaut False, False*'BLOCK' donne "", puis "or 'WAIT'" donne "WAIT".
