#Exercice 1 

# Demande d'informations à l'utilisateur
prenom = input("Entrez votre prénom :  ")
age = int(input("Entrez votre âge: "))
ville = input("Entrez votre ville: ")
metier = input("Entrez votre métier: ")

#Approximation des jours vécus 
jours_vecus = age * 365

#Affichage formaté
print("\n=== PROFIL UTILISATEUR ===")
print(f"Prénom: {prenom}")
print(f"Âge: {age} ans ({jours_vecus} jours vécus environ)")
print(f"Ville: {ville}")
print(f"Métier: {metier}")

#Exercice 2 

# Définition des variables
nom_produit = "Casque Bluetooth"
prix = 150.0
stock = 35
remise = 0.15  # 15%

# Calcul du prix final
prix_final = prix * (1 - remise)

# Affichage
print(f"Produit : {nom_produit}")
print(f"Prix initial : {prix} €")
print(f"Remise : {remise * 100}%")
print(f"Prix final : {prix_final:.2f} €")
print(f"Stock disponible : {stock}")

#Exercice 3 

# Entrée utilisateur
heures = int(input("Nombre d'heures: "))
minutes = int(input("Nombre de minutes: "))
secondes = int(input("Nombre de secondes: "))

# Conversion
total_secondes = heures * 3600 + minutes * 60 + secondes

# Résultat
print(f"Durée totale: {total_secondes} secondes.")

#Exercice 4 

note_20 = float(input("Note sur 20: "))
note_100 = (note_20 / 20) * 100

print(f"Note sur 100 : {note_100:.1f}")

#Exercice 5

distance_km = float(input("Distance (km): "))
temps_h = float(input("Temps (heures): "))

vitesse_kmh = distance_km / temps_h
vitesse_ms = (distance_km * 1000) / (temps_h * 3600)

print(f"Vitesse moyenne: {vitesse_kmh:.2f} km/h")
print(f"Vitesse moyenne: {vitesse_ms:.2f} m/s")

