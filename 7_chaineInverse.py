import sys

if len(sys.argv) < 2:
    print("Erreur: pas d'argumets")

userInput = " ".join(sys.argv[1:])
inverse = ""

for letter in userInput:
    inverse = letter + inverse

print(inverse)