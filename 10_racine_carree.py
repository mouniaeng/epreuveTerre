import sys

if len(sys.argv) != 2 : 
    print("Erreur: Veuillez rentrer un arguments.")
elif not sys.argv[1].isdigit():
   print("Erreur: Ne rentrez que un nombre.")
else:
 input = int(sys.argv[1])
 total = input **0.5
 print(total)