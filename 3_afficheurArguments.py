#utilisé pour récupérer les arguments passés en ligne de commande.
import sys

#boucle for: pour chaque argument rentre, en commencent par le "premier" d'ou le sys.arg[1:], afficher l'argument
for arg in sys.argv[1:]:
    print(arg)



#import sys
#print("\n".join(sys.argv[1:]))