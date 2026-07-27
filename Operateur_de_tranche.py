# Exercice 1 
mot = input("Entrez un mot (min. 5 lettres): ")

if len(mot) >= 5:
    milieu = mot[2:-2]
    print(f"Partie centrale: {milieu}")
else:
    print("Mot trop court.")

# Exercice 2
entree = input("Entrez des éléments séparés par des espaces: ")
liste = entree.split()

liste_inversee = liste[::-1]
print(f"Liste inversée: {liste_inversee}")

# Exercice 3 
phrase = input("Entrez une phrase: ")
mots = phrase.split()

un_sur_deux = mots[::2]
print(f"Mots un sur deux: {un_sur_deux}")

# Exercice 4
numero = input("Entrez un numéro de téléphone: ")

if len(numero) > 3:
    masque = "*" * (len(numero) - 3) + numero[-3:]
    print(f"Numéro masqué: {masque}")
else:
    print("Numéro trop court pour masquer.")

# Exercice 5 
entree = input("Entrez des nombres séparés par des espaces: ")
liste = entree.split()

indices_pairs = liste[::2]
print(f"Éléments aux indices pairs: {indices_pairs}")
