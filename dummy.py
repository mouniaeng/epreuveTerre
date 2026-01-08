import sys

#CONDITIONS:
if len(sys.argv) < 1:
    print("Erreur : vous devez passer un argument.")
# oblige de mettre le sys.exit(1) ?
elif len(sys.argv) > 2:
    print("Erreur: ne rentrez qu'un seul argument.")
elif len(sys.argv) == int:
    print("Erreur : passez une lettre minuscule de l'alphabet.")
else :
    print("oki")


