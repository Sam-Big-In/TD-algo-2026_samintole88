# Exercice 1 
nombre = int(input("Entrez un nombre pour sa table de multiplication: "))

print(f"=== Table de {nombre} ===")
for i in range(1, 13):
    resultat = nombre * i
    print(f"{nombre} x {i} = {resultat}")

# Exercice 2 
entree = input("Entrez des nombres séparés par des espaces: ")
liste = [int(x) for x in entree.split()]

somme_pairs = 0
for nombre in liste:
    if nombre % 2 == 0:
        somme_pairs += nombre

print(f"Somme des nombres pairs: {somme_pairs}")

# Exercice 3 
texte = input("Entrez une chaîne: ")
inverse = ""

for char in texte:
    inverse = char + inverse

print(f"Chaîne inversée: {inverse}")

# Exercice 4 
carres = []

for i in range(1, 21):
    carres.append(i ** 2)

print("Tous les carrés:", carres)
print("Carrés > 100:")
for val in carres:
    if val > 100:
        print(val)

# Exercice 5 
mots = input("Entrez des mots séparés par des espaces: ").split()
voyelles = "aeiouyAEIOUY"
total_voyelles = 0

for mot in mots:
    for lettre in mot:
        if lettre in voyelles:
            total_voyelles += 1

print(f"Nombre total de voyelles: {total_voyelles}")
