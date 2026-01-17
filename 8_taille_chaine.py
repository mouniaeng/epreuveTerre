import sys

if len(sys.argv) != 2 : 
    print("Erreur: Veuillez rentrer un argument.")
elif not sys.argv[1].isalpha(): 
    print("Erreur: Veuillez ne rentrer que des lettres.")
else :
    input = sys.argv[1]
    total = 0

    for letter in input :
     total = total + 1

    print(total)



