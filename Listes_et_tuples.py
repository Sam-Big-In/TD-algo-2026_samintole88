# Exercice 1 
entree = input("Entrez des nombres séparés par des espaces: ")
liste = [int(x) for x in entree.split()]

n = len(liste)
for i in range(n):
    for j in range(0, n - i - 1):
        if liste[j] > liste[j + 1]:
            liste[j], liste[j + 1] = liste[j + 1], liste[j]

print(f"Liste triée: {liste}")

# Exercice 2
entree = input("Entrez des valeurs séparées par des espaces: ")
liste = entree.split()

uniques = []
for item in liste:
    if item not in uniques:
        uniques.append(item)

print(f"Valeurs uniques: {uniques}")

# Exercice 3 
entree = input("Entrez des nombres: ")
liste = [float(x) for x in entree.split()]

if liste:
    maximum = max(liste)
    minimum = min(liste)
    moyenne = sum(liste) / len(liste)

    print(f"Maximum: {maximum}")
    print(f"Minimum: {minimum}")
    print(f"Moyenne: {moyenne:.2f}")
else:
    print("La liste est vide.")
  
  # Exercice 4 
etudiants = [
    ("Alice", 16),
    ("Bob", 12),
    ("Charlie", 18),
    ("David", 14),
    ("Eve", 15)
]

print("Étudiants avec une note >= 15:")
for nom, note in etudiants:
    if note >= 15:
        print(f"- {nom}: {note}/20")

# Exercice 5 
entree = input("Entrez des éléments: ")
liste = entree.split()

liste_inversee = []
for i in range(len(liste) - 1, -1, -1):
    liste_inversee.append(liste[i])

print(f"Liste inversée: {liste_inversee}")
