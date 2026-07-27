# Exercice 1 
age = int(input("Entrez votre âge: "))
pays = input("Entrez votre pays: ").lower()

if age >= 18 and (pays == "congo" or pays == "cameroun"):
    print("Inscription autorisée.")
elif age < 18:
    print("Vous devez être majeur pour vous inscrire.")
else:
    print("Désolé, programme réservé aux ressortissants du Congo ou du Cameroun.")
  
# Exercice 2 
note = float(input("Entrez votre note sur 100: "))

if note >= 90:
    print("Mention: Excellent")
elif note >= 75:
    print("Mention: Très Bien")
elif note >= 60:
    print("Mention: Bien")
elif note >= 50:
    print("Mention: Passable")
else:
    print("Mention: Insuffisant")

# Exercice 3
panier = float(input("Montant du panier (€): "))

if panier >= 100:
    frais = 0
elif panier >= 50:
    frais = 5
else:
    frais = 10

total = panier + frais
print(f"Frais de livraison: {frais} €")
print(f"Total à payer: {total:.2f} €")

# Exercice 4 
temp = float(input("Température (°C): "))

if temp >= 35:
    print("Très chaud, restez hydraté.")
elif temp >= 25:
    print("Chaud, faites attention au soleil.")
elif temp >= 15:
    print("Température agréable.")
else:
    print("Il fait frais, couvrez-vous.")

# Exercice 5 
mdp = input("Entrez un mot de passe: ")

if len(mdp) >= 8 and any(c.isdigit() for c in mdp) and any(c.isupper() for c in mdp):
    print("Mot de passe valide.")
else:
    print("Mot de passe invalide.")
