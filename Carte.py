class Carte:
    """
    Classe définissant la carte sous forme de liste d'après un fichier .txt passé en entrée.
    Une méthode de mouvement est définie pour chaque direction. Ces méthodes sont appelées par une autre méthode, qui
    demande sa prochaine action au joueur.

    """

    def __init__(self, chaine):
        """
        Constructeur de la classe Carte : on lit un fichier .txt à partir du choix du joueur
        La carte est stockée sous forme de chaîne de caractères.

        Paramètres :
        - labyrinthe : la carte, stockée sous forme de chaîne de caractères
        - case_victorieuse : on enregistre l'index de la sortie, 'U'. Si, à cet index, on a un autre symbole, cela
                             signifie que la partie est gagnée
        - quitter : un booléen qui passe à 'True' si le choix choisit de quitter la partie
        - largeur : la largeur de la carte, utilisée pour les mouvements verticaux. On suppose que la carte est de
        largeur constante (rectangulaire), et on compte le retour à la ligne

        """
        if 'txt' in chaine:
            fichier = open(chaine, 'r')
            self.labyrinthe = fichier.read()
            fichier.close()
        else:
            self.labyrinthe = chaine

        self.case_victorieuse = self.labyrinthe.find('U')
        self.quitter = False
        self.largeur = len(self.labyrinthe.split('\n')[0]) + 1

    def prochain_mvt(self):
        """
        Méthode appelée afin de demander son prochain mouvement au joueur.
        On distingue le choix (= direction) et la longueur désirée du mouvement

        """
        mouvement = input("Quel mouvement souhaitez-vous effectuer ?")
        choix = mouvement[0]

        if len(mouvement) == 1:
            longueur = 1
        else:
            longueur = int(mouvement[1:])

        if choix.upper() == 'N':
            [self.move_up() for _ in range(longueur)]  # permet de répéter la méthode de mouvement "longueur" fois
        elif choix.upper() == 'E':
            [self.move_right() for _ in range(longueur)]
        elif choix.upper() == 'O':
            [self.move_left() for _ in range(longueur)]
        elif choix.upper() == 'S':
            [self.move_down() for _ in range(longueur)]
        elif choix.upper() == 'Q':
            self.quitter = True
        else:
            print("Ce mouvement n'est pas valide")

    def move_up(self):
        """
        Fonction permettant au robot de se déplacer vers le haut
        La chaîne matérialisant le labyrinthe est convertie en liste afin qu'on puisse modifier ses éléments

        """
        position_actuelle = self.labyrinthe.index('X')
        prochaine_position = self.labyrinthe.index('X') - self.largeur
        nouvelle_carte = list(self.labyrinthe)  # on transforme la chaîne de caractères en liste

        if nouvelle_carte[prochaine_position] == 'O':
            print("Vous ne pouvez pas effectuer ce mouvement")
        else:
            nouvelle_carte[position_actuelle] = " "
            nouvelle_carte[prochaine_position] = "X"
        self.labyrinthe = ''.join(nouvelle_carte)  # liste --> chaîne de caractères

    def move_right(self):
        """
        Fonction permettant au robot de se déplacer vers la droite
        La chaîne matérialisant le labyrinthe est convertie en liste afin qu'on puisse modifier ses éléments

        """
        position_actuelle = self.labyrinthe.index('X')
        prochaine_position = self.labyrinthe.index('X') + 1
        nouvelle_carte = list(self.labyrinthe)

        if nouvelle_carte[prochaine_position] in ('O', '\n'):
            print("Vous ne pouvez pas effectuer ce mouvement")
        else:
            nouvelle_carte[position_actuelle] = " "
            nouvelle_carte[prochaine_position] = "X"
        self.labyrinthe = ''.join(nouvelle_carte)

    def move_left(self):
        """
        Fonction permettant au robot de se déplacer vers la gauche
        La chaîne matérialisant le labyrinthe est convertie en liste afin qu'on puisse modifier ses éléments

        """
        position_actuelle = self.labyrinthe.index('X')
        prochaine_position = self.labyrinthe.index('X') - 1
        nouvelle_carte = list(self.labyrinthe)

        if nouvelle_carte[prochaine_position] in ('O', '\n'):
            print("Vous ne pouvez pas effectuer ce mouvement")
        else:
            nouvelle_carte[position_actuelle] = " "
            nouvelle_carte[prochaine_position] = "X"
        self.labyrinthe = ''.join(nouvelle_carte)

    def move_down(self):
        """
        Fonction permettant au robot de se déplacer vers le bas
        La chaîne matérialisant le labyrinthe est convertie en liste afin qu'on puisse modifier ses éléments

        """
        position_actuelle = self.labyrinthe.index('X')
        prochaine_position = self.labyrinthe.index('X') + self.largeur
        nouvelle_carte = list(self.labyrinthe)

        if nouvelle_carte[prochaine_position] == 'O':
            print("Vous ne pouvez pas effectuer ce mouvement")
        else:
            nouvelle_carte[position_actuelle] = " "
            nouvelle_carte[prochaine_position] = "X"
        self.labyrinthe = ''.join(nouvelle_carte)

    def victoire(self):
        """
        Méthode permettant de déterminer si la partie est victorieuse, appelée après chaque mouvement du joueur.
        Renvoie 'True" en cas de victoire

        """
        if self.labyrinthe[self.case_victorieuse] == 'X':
            return True
        else:
            return False
