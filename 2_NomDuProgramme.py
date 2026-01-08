import os                                      # permet d'interagir avec le OS

chemin_complet=__file__                        # chemin_complet est une variable qu'on accorde a __file__, __file__ est le chemin complet du fichier

nom_fichier=os.path.basename(chemin_complet)   # nom_fichier nouvelle variable qui s'accorde avec la focntion os.path.basename(),
                                               #la fonction os.path.basename() affiche seulement le nom du fichier du chemin complet.

print(nom_fichier)