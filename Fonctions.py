# Exercice 1
def calculer(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b != 0:
            return a / b
        else:
            return "Division par zéro impossible."
    else:
        return "Opérateur non valide."

x = float(input("Nombre 1: "))
y = float(input("Nombre 2: "))
operation = input("Opération (+, -, *, /): ")

resultat = calculer(x, y, operation)
print(f"Résultat: {resultat}")

# Exercice 2 
def statistiques(liste):
    if not liste:
        return 0, 0, None
    s = sum(liste)
    m = s / len(liste)
    mx = max(liste)
    return s, m, mx

nombres = [float(x) for x in input("Entrez des nombres: ").split()]
somme, moyenne, maximum = statistiques(nombres)
print(f"Somme: {somme}, Moyenne: {moyenne:.2f}, Max: {maximum}")

# Exercice 3
def est_palindrome(mot):
    mot_epure = mot.lower().replace(" ", "")
    return mot_epure == mot_epure[::-1]

mot_test = input("Entrez un mot: ")
if est_palindrome(mot_test):
    print(f"'{mot_test}' est un palindrome.")
else:
    print(f"'{mot_test}' n'est pas un palindrome.")

# Exercice 4 
def convertir(usd):
    eur = usd * 0.93
    cfa = usd * 610
    gbp = usd * 0.79
    return eur, cfa, gbp

montant = float(input("Montant en USD: "))
eur, cfa, gbp = convertir(montant)
print(f"{montant} USD = {eur:.2f} EUR, {cfa:.2f} CFA, {gbp:.2f} GBP")

# Exercice 5 
import random
import string

def generer_mdp(longueur):
    caracteres = string.ascii_letters + string.digits
    mdp = "".join(random.choice(caracteres) for _ in range(longueur))
    return mdp

longueur = int(input("Longueur du mot de passe: "))
print(f"Mot de passe généré: {generer_mdp(longueur)}")
