import sys

if len(sys.argv) != 3 : 
    print("Erreur: Veuillez rentrer deux arguments.")
elif not sys.argv[1].isdigit():
    print("Erreur: Ne rentrez que des nombres.")
elif not sys.argv[2].isdigit():
    print("Erreur: Ne rentrez que des nombres.")
else :
    input_one = int(sys.argv[1])
    input_two = int(sys.argv[2])
    total = input_one ** input_two

    print(total)