import random

#variable

nombre_aleatoire = random.randint(0,50)
nombre_essais = 5
essais_restant = 0
while True :
    nombre_utilisateur = input("Devine le nombre : ")
    nombre_essais -= 1
    while not nombre_utilisateur.isdigit():
        nombre_utilisateur = input("Devine le nombre : ")
    else:
        nombre_verifier = int(nombre_utilisateur)

    if nombre_verifier < nombre_aleatoire:
        print(f"Le nombre mystere est plus grand que {nombre_utilisateur}")
        print(f"Il te reste {nombre_essais} essais")
        essais_restant +=1

    elif nombre_verifier > nombre_aleatoire:
        print(f"Le nombre mystere est plus petit que {nombre_utilisateur}")
        print(f"Il te reste {nombre_essais} essais")
        essais_restant += 1

    elif nombre_verifier == nombre_aleatoire:
        print(f"Bravo ! le nombre mystere était bien {nombre_aleatoire}")
        print(f"Tu as trouver le nombre en {essais_restant}")
        print("Fin du jeu")
        break

    if nombre_essais == 0:
        print(f"Dommage ! Le nombre mystere etait {nombre_aleatoire} ")
        print("fin du jeu.")
        break