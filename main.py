import random

mot = ["chaussette", "feuille", "fourchette", "lit"]

mot_aléatoire = random.choice(mot)
Nombre_de_vie = 5
lettres_trouvées = []

while Nombre_de_vie > 0:
    mot_partiel = ""
    for lettre in mot_aléatoire:
        if lettre in lettres_trouvées:
            mot_partiel = mot_partiel + lettre
        else:
            mot_partiel = mot_partiel + "_"
    
    print("Mot actuel: ", mot_partiel)

    if "_" not in mot_partiel:
        print("Félicitation vous avez trouvé le mot {} !".format(mot_aléatoire))
        break

    lettre = input("Choisir une lettre: ").lower()
    if len(lettre) == 1 and lettre.isalpha():
        if lettre in lettres_trouvées:
            print("Vous avez déjà trouvé cette lettre")
        elif lettre in mot_aléatoire:
            print("La lettre {} est présente dans le mot à trouver".format(lettre))
            lettres_trouvées.append(lettre)
        else:
            Nombre_de_vie = Nombre_de_vie - 1
            print("Il vous reste {} vies".format(Nombre_de_vie))
    else:
        print("Veuillez choisir une seule lettre")


if Nombre_de_vie == 0:
    print("Vous avez perdu, le mot a trouver était {} !".format(mot_aléatoire))
    

