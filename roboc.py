""" Script à exécuter pour jouer au jeu du labyrinthe
Complétion de la doc
Nouveau test de commit
"""
from Carte import Carte
import os
import pickle

# on récupère le dossier courant, où est exécuté le script
path = os.getcwd()

# paramètre à modifier en fonction du nom du dossier où se trouvent les cartes
maps_folder_name = 'cartes'

# chemin complet vers les cartes
maps_folder = os.path.join(path, maps_folder_name)

# chemin complet vers la partie sauvegardée
saved_file = os.path.join(maps_folder, 'partie_sauvegardee')

# on stocke les cartes disponibles, sans extension
available_maps = [os.path.splitext(c)[0] for c in os.listdir(maps_folder)
                  if os.path.isfile(os.path.join(maps_folder, c))
                  and c != 'partie_sauvegardee']

# on fait un dict : chaque entier correspond à une carte
maps_dict = {i + 1: m for i, m in enumerate(available_maps)}

# ce booléen sert à déterminer si on doit continuer de jouer ou pas
continuer = True

# on regarde s'il existe déjà une partie sauvegardée : initialisé à 'True' si c'est le cas, 'False' sinon
sauvegarde = os.path.isfile(saved_file)

# booléen qui passe à True si une exception est levée
error = False


def std_display():
    """
    Fonction d'affichage classique, qui allège un peu le corps du script.
    Cette fonction instancie l'objet carte sur lequel on travaille.

    """
    print("Veuillez choisir votre carte :\n")
    for k, v in maps_dict.items():
        print(f'{k}. {v}')
    no_carte = int(input("Carte choisie :"))
    carte_choisie = maps_dict[no_carte] + '.txt'
    global carte
    carte = Carte(os.path.join(maps_folder, carte_choisie))


print("Bienvenue dans le jeu du labyrinthe !\n")

# si une partie sauvegardée existe, on propose de la continuer. Sinon, on utilise l'affichage standard
if sauvegarde:
    continuer = input("Une partie est en cours. Voulez-vous la continuer ? O/N")
    if continuer.upper() == 'O':
        with open(saved_file, 'rb') as file:
            mon_depickler = pickle.Unpickler(file)
            carte_recuperee = mon_depickler.load()
        carte = Carte(carte_recuperee)
    else:
        try:
            std_display()
        except (ValueError, KeyError, NameError):
            print("Cette carte n'est pas disponible")
            error = True
else:
    try:
        std_display()
    except (ValueError, KeyError, NameError):
        print("Cette carte n'est pas disponible")
        error = True

if not error:
    while not carte.quitter:
        print('\n' + carte.labyrinthe + '\n')
        carte.prochain_mvt()
        with open(saved_file, 'wb') as file:
            pickle.dump(carte.labyrinthe, file)
        if carte.victoire():
            print("Félicitations, vous avez gagné !")
            os.remove(saved_file)  # on supprime la sauvegarde si le jeu est gagné
            carte.quitter = True
