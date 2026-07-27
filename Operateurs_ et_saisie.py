# Exercice 1
a = float(input("Entrez le premier nombre: "))
b = float(input("Entrez le deuxième nombre: "))

somme = a + b
difference = a - b
produit = a * b
quotient = a / b if b != 0 else "Division par zéro"
division_entiere = a // b if b != 0 else "Division par zéro"
reste = a % b if b != 0 else "Division par zéro"

print(f"Somme: {somme}")
print(f"Différence: {difference}")
print(f"Produit: {produit}")
print(f"Quotient: {quotient}")
print(f"Division entière: {division_entiere}")
print(f"Reste: {reste}")

# Exercice 2
n = int(input("Entrez un nombre entier: "))

if n % 3 == 0 and n % 5 == 0:
    print("Le nombre est divisible par 3 et 5.")
else:
    print("Le nombre n'est pas divisible par 3 et 5 à la fois.")

# Exercice 3
montant_ht = float(input("Montant HT (€): "))
taux_tva = float(input("Taux de TVA (%): "))

taux_coef = taux_tva / 100
montant_ttc = montant_ht * (1 + taux_coef)

print(f"Montant TTC: {montant_ttc:.2f} €")

# Exercice 4 
note1 = float(input("Première note: "))
note2 = float(input("Deuxième note: "))
note3 = float(input("Troisième note: "))

moyenne = (note1 + note2 + note3) / 3
print(f"Moyenne: {moyenne:.2f}")

if moyenne >= 10:
    print("L'étudiant est reçu.")
else:
    print("L'étudiant n'est pas reçu.")

# Exercice 5 
usd = float(input("Montant en USD: "))

eur = usd * 0.93
cfa = usd * 610
gbp = usd * 0.79

print(f"{usd} USD = {eur:.2f} EUR")
print(f"{usd} USD = {cfa:.2f} CFA")
print(f"{usd} USD = {gbp:.2f} GBP")
