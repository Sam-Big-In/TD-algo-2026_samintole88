# Exercice 1 
import random

nombre_secret = random.randint(1, 100)
essai = None

while essai != nombre_secret:
    essai = int(input("Devine le nombre (1-100): "))
    if essai < nombre_secret:
        print("Trop petit.")
    elif essai > nombre_secret:
        print("Trop grand.")
    else:
        print("Bravo, tu as trouvé !")

# Exercice 2 
choix = ""

while choix != "0":
    print("\n=== MENU ===")
    print("1. Dire Bonjour")
    print("2. Additionner deux nombres")
    print("0. Quitter")
    
    choix = input("Choisissez une option: ")
    
    if choix == "1":
        print("Bonjour !")
    elif choix == "2":
        a = float(input("Nombre 1: "))
        b = float(input("Nombre 2: "))
        print(f"Résultat: {a + b}")
    elif choix == "0":
        print("Au revoir !")
    else:
        print("Choix invalide.")
      
# Exercice 3 
somme = 0
nb_notes = 0

while True:
    note = float(input("Entrez une note (-1 pour arrêter): "))
    if note == -1:
        break
    somme += note
    nb_notes += 1

if nb_notes > 0:
    moyenne = somme / nb_notes
    print(f"Moyenne des notes: {moyenne:.2f}")
else:
    print("Aucune note saisie.")

# Exercice 4 
mdp = ""

while mdp != "Python2025":
    mdp = input("Entrez le mot de passe: ")
    if mdp == "Python2025":
        print("Accès autorisé.")
    else:
        print("Mot de passe incorrect, réessayez.")

# Exercice 5 
n = int(input("Entrez un entier positif: "))

while n < 0:
    print("Veuillez entrer un nombre positif.")
    n = int(input("Entrez un entier positif: "))

fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1

print(f"Factorielle de {n} = {fact}")
