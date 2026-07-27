# Exercice 1 
texte = input("Entrez un texte: ")

texte_propre = texte.strip().lower().replace(".", "!")
print(f"Texte nettoyé: {texte_propre}")

# Exercice 2
email = input("Entrez une adresse email: ").strip()

if email.endswith("@gmail.com"):
    print("Adresse Gmail valide.")
else:
    print("L'adresse email doit se terminer par '@gmail.com'.")

# Exercice 3 
texte = input("Entrez un texte: ")
mot = input("Entrez le mot à chercher: ")

occurrences = texte.lower().count(mot.lower())
print(f"Le mot '{mot}' apparaît {occurrences} fois.")

# Exercice 4
phrase = input("Entrez une phrase: ")
mots = phrase.split()

acronyme = "".join([m[0].upper() for m in mots if m])
print(f"Acronyme: {acronyme}")

# Exercice 5 
phrase = input("Entrez une phrase: ")
mot = input("Mot à masquer: ")

masque = "*" * len(mot)
nouvelle_phrase = phrase.replace(mot, masque)

print(f"Phrase après masquage: {nouvelle_phrase}")
