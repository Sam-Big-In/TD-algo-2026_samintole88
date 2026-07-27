# Exercice 1 
utilisateurs = []

while True:
        nom = input("Entrez un nom d'utilisateur ('stop' pour finir): ")
        if nom.lower() == "stop":
            break   
        utilisateur.append(nom)
with open("utilisateurs.txt", "w", encoding="utf-8") as f:
    for u in utilisateur : 
        f.write(nom + "\n")

print("Utilisateurs enregistrés dans 'utilisateurs.txt'.")

#Exercice 2
nombre = int(input("Nombre pour la table de multiplication : "))

with open("table.txt", "w", encoding="utf-8") as f:
    for i in range(1, 13):
        ligne = f"{nombre} x {i} = {nombre * i}\n"
        f.write(ligne)

print("Table générée dans 'table.txt'.")

#Exercice 3 
activite = input("Saisissez votre activité du jour : ")

with open("journal.txt", "a", encoding="utf-8") as f:
    f.write(activite + "\n")

print("Activité ajoutée dans 'journal.txt'.")

#Exercice 4
notes = [float(x) for x in input("Entrez des notes : ").split()]
moyenne = sum(notes) / len(notes)

with open("statistiques.txt", "w", encoding="utf-8") as f:
    f.write(f"Notes : {notes}\n")
    f.write(f"Moyenne : {moyenne:.2f}\n")

print("Statistiques sauvegardées dans 'statistiques.txt'.")

#Exercice 5 
texte = input("Entrez une phrase : ")

nb_mots = len(texte.split())
nb_caracteres = len(texte)

with open("rapport.txt", "w", encoding="utf-8") as f:
    f.write("=== Rapport d'analyse texte ===\n")
    f.write(f"Phrase : {texte}\n")
    f.write(f"Nombre de mots : {nb_mots}\n")
    f.write(f"Nombre de caractères : {nb_caracteres}\n")

print("Rapport sauvegardé dans 'rapport.txt'.")
