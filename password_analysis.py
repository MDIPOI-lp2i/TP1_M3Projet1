# password_analysis.py
import re

while True:
    # Demande à l'utilisateur d'entrer un mot de passe
    password = input("Entrez un mot de passe : ")

    # Vérifier la longueur du mot de passe
    if len(password) < 8:
        print("Le mot de passe doit contenir au moins 8 caractères.")
        continue
    # Vérifier si le mot de passe contient au moins une majuscule
    if not re.search(r"[A-Z]", password):
        print("Le mot de passe doit contenir au moins une majuscule.")
        continue
    # Vérifier si le mot de passe contient au moins un chiffre
    if not re.search(r"[0-9]", password):
        print("Le mot de passe doit contenir au moins un chiffre.")
        continue
    # Vérifier si le mot de passe contient au moins un caractère spécial
    if not re.search(r"[@#$%^&*!]", password):
        print("Le mot de passe doit contenir au moins un caractère spécial.")
        continue
    
    # Si toutes les conditions sont respectées
    print("Le mot de passe est robuste.")
    break
