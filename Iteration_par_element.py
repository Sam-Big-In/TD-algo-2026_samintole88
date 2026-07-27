# Exercice 1 
livres = [
    {"titre": "Python débutant", "auteur": "Dupont", "année": 2008},
    {"titre": "Maîtriser Python", "auteur": "Durand", "année": 2015},
    {"titre": "Python avancé", "auteur": "Martin", "année": 2021}
]

print("Livres publiés après 2010:")
for livre in livres:
    if livre["année"] > 2010:
        print(f"- {livre['titre']} ({livre['année']}) par {livre['auteur']}")

# Exercice 2 
entree = input("Entrez des éléments: ")
liste = entree.split()

for i, elem in enumerate(liste):
    print(f"Indice {i}: {elem}")

# Exercice 3 
matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for ligne in matrice:
    for element in ligne:
        print(element, end=" ")
    print()  # saut de ligne

# Exercice 4 
phrase = input("Entrez une phrase: ")
mots = phrase.split()
count = 0

for mot in mots:
    if len(mot) > 5:
        count += 1

print(f"Nombre de mots > 5 lettres: {count}")

# Exercice 5 
texte = input("Entrez un texte: ")
voyelles = "aeiouyAEIOUY"

print("Consonnes: ", end="")
for char in texte:
    if char.isalpha() and char not in voyelles:
        print(char, end="")
