#Exercice 1 
try:
    a = float(input("Nombre 1 : "))
    b = float(input("Nombre 2 : "))
    result = a / b
except ZeroDivisionError:
    print("Erreur : Division par zéro !")
else:
    print(f"Résultat : {result}")
#Exercice 2
valeur = input("Entrez un entier : ")

try:
    entier = int(valeur)
except ValueError:
    print("Erreur : ce n'est pas un entier valide.")
else:
    print(f"Vous avez entré l'entier : {entier}")

#Exercice 3
nom_fichier = input("Nom du fichier à lire : ")

try:
    with open(nom_fichier, "r", encoding="utf-8") as f:
        contenu = f.read()
except FileNotFoundError:
    print("Erreur : Fichier introuvable.")
else:
    print("Contenu du fichier :")

#Exercice 4
while True:
    try:
        n = int(input("Entrez un entier positif : "))
        if n < 0:
            raise ValueError("Nombre négatif interdit.")
        break
    except ValueError as e:
        print(f"Erreur : {e}")

print(f"Vous avez saisi : {n}")

# Exercice 5
import math

try:
    x = float(input("Entrez un nombre : "))
    if x < 0:
        raise ValueError("Nombre négatif, pas de racine réelle.")
    racine = math.sqrt(x)
except ValueError as e:
    print(f"Erreur : {e}")
else:
    print(f"Racine carrée : {racine}")
finally:
    print("Fin du calcul.")
    print(contenu)
