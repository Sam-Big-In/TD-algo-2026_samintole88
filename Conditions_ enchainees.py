# Exercice 1 
age = int(input("Âge: "))
statut = input("Statut (étudiant/salarié/retraité): ").lower()

if age < 18:
    tarif = 5
else:
    if 18 <= age <= 25:
        if statut == "étudiant" or statut == "etudiant":
            tarif = 6
        elif statut == "salarié" or statut == "salarie":
            tarif = 8
        else:
            tarif = 10
    else:
        if statut == "retraité" or statut == "retraite":
            tarif = 7
        else:
            tarif = 10

print(f"Tarif de votre abonnement: {tarif} €")

# Exercice 2 
role = input("Rôle (employé/visiteur/sécurité): ").lower()

if role == "employé" or role == "employe":
    badge = input("Badge valide? (oui/non): ").lower()
    if badge == "oui":
        print("Accès autorisé.")
    else:
        print("Accès refusé, badge invalide.")
elif role == "visiteur":
    rdv = input("Avez-vous un rendez-vous? (oui/non): ").lower()
    if rdv == "oui":
        print("Accès autorisé.")
      
# Exercice 3
fievre = input("Avez-vous de la fièvre? (oui/non): ").lower()

if fievre == "oui":
    douleurs = input("Avez-vous des douleurs? (oui/non): ").lower()
    if douleurs == "oui":
        print("Consulter un médecin.")
    else:
        print("Surveiller les symptômes.")
else:
    toux = input("Avez-vous de la toux? (oui/non): ").lower()
    if toux == "oui":
        print("Repos conseillé.")
    else:
        print("Bonne santé.")
    else:
        print("Accès refusé, pas de rendez-vous.")
elif role == "sécurité" or role == "securite":
    print("Accès autorisé.")
else:
    print("Accès refusé, rôle inconnu.")

# Exercice 4 
anciennete = int(input("Années d'ancienneté: "))
note = int(input("Note de performance (1 à 5): "))

if anciennete >= 5:
    if note >= 4:
        prime = 2000
    else:
        prime = 1000
else:
    if note >= 4:
        prime = 500
    else:
        prime = 0

print(f"Prime attribuée: {prime} €")

# Exercice 5 
plat = input("Choix du plat (viande/poisson/végétarien): ").lower()

if plat == "viande":
    cuisson = input("Cuisson (saignant/à point/bien cuit): ").lower()
    print(f"Vous avez commandé une viande {cuisson}.")
elif plat == "poisson":
    sauce = input("Sauce (citron/beurre): ").lower()
    print(f"Vous avez commandé un poisson sauce {sauce}.")
elif plat == "végétarien" or plat == "vegetarien":
    choix = input("Souhaitez-vous une salade ou des pâtes?: ").lower()
    print(f"Vous avez commandé: {choix}.")
else:
    print("Choix invalide.")








