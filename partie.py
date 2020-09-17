__authors__ = "boutheyna salah & khouloud sadghriani FIA1 G01"
__date__ = "09/12/2018"

"""Ce fichier permet de...(complétez la description de ce que
ce fichier est supposé faire ! """

from plateau import Plateau
from joueur import Joueur

class Partie:
    """
    Classe modélisant une partie du jeu Tic-Tac-Toe utilisant
    un plateau et deux joueurs (deux personnes ou une personne et un ordinateur).

    Attributes:
        plateau (Plateau): Le plateau du jeu contenant les 9 cases.
        joueurs (Joueur list): La liste des deux joueurs (initialement une liste vide).
        joueur_courant (Joueur): Le joueur courant (initialisé à une valeur nulle: None)
        nb_parties_nulles (int): Le nombre de parties nulles (aucun joueur n'a gagné).
    """

    def __init__(self):
        """
        Méthode spéciale initialisant une nouvelle partie du jeu Tic-Tac-Toe.
        """
        self.plateau = Plateau()    # Le plateau du jeu contenant les 9 cases.
        self.joueurs = []       # La liste des deux joueurs (initialement une liste vide).
                                # Au début du jeu, il faut ajouter les deux joueurs à cette liste.
        self.joueur_courant = None  # Le joueur courant (initialisé à une valeur nulle: None)
                                    # Pendant le jeu et à chaque tour d'un joueur,
                                    # il faut affecter à cet attribut ce joueur courant.
        self.nb_parties_nulles = 0  # Le nombre de parties nulles (aucun joueur n'a gagné).

    def jouer(self):
        """
        Permet de démarrer la partie en commençant par l'affichage de ce texte:

        Bienvenue au jeu Tic Tac Toe.
        ---------------Menu---------------
        1- Jouer avec l'ordinateur.
        2- Jouter avec une autre personne.
        0- Quitter.
        -----------------------------------
        Entrez s.v.p. un nombre entre 0 et 2:?

        Cette méthode doit donc utiliser la méthode saisir_nombre().
        Elle doit par la suite demander à l'utilisateur les noms des joueurs.
        Veuillez utiliser 'Colosse' comme nom pour l'ordinateur.
        Il faut créer des instances de la classe Joueur et les ajouter à la liste joueurs.
        Il faut utiliser entre autres ces méthodes:
            *- demander_forme_pion(): pour demander au premier joueur la forme de son pion (X ou O).
              (Pas besoin de demander à l'autre joueur ou à l'ordinateur cela, car on peut le déduire).
            *- plateau.non_plein(): afin d'arrêter le jeu si le plateau est plein (partie nulle).
            *- tour(): afin d'exécuter le tour du joueur courant.
            *- plateau.est_gagnant(): afin de savoir si un joueur a gagné et donc arrêter le jeu.
        Il faut alterner entre le premier joueur et le deuxième joueur à chaque appel de tour()
        en utilisant l'attribut joueur_courant.
        Après la fin de chaque partie, il faut afficher les statistiques sur le jeu.
        Voici un exemple:

        Partie terminée! Le joueur gagnant est: Colosse
        Parties gagnées par Mondher : 2
        Parties gagnées par Colosse : 1
        Parties nulles: 1
        Voulez-vous recommencer (O,N)?

        Il ne faut pas oublier d'initialiser le plateau avant de recommencer le jeu.
        Si l'utilisateur ne veut plus recommencer, il faut afficher ce message:
        ***Merci et au revoir !***
        """

        print( "Bienvenue au jeu Tic Tac Toe.")
        print("---------------Menu---------------")
        print("1- Jouer avec l'ordinateur.")
        print("2- Jouter avec une autre personne.")
        print("0- Quitter.")
        print("-----------------------------------")

        print("svp entrez votre choix")
        choix = self.saisir_nombre(0,3)

        if(choix == 1):
            print("SVP entrer votre nom : ")
            nom = input()
            print(nom," SVP entrer votre pion : ")
            pion = self.demander_forme_pion()
            joueur1 = Joueur(nom,"Personne",pion)
            self.joueurs.append(joueur1)

            if(joueur1.pion == "X"):
                joueur2 = Joueur("Colosse","Ordinateur","O")
                self.joueurs.append(joueur2)
            else:
                joueur2 = Joueur("Colosse","Ordinateur","X")
                self.joueurs.append(joueur2)

            self.joueur_courant = self.joueurs[0]
            rep = ""
            
            while ( rep.upper() != "N" ):
                self.plateau = Plateau()
                print(self.plateau.__str__())
                while (self.plateau.non_plein()):
                    self.tour(choix)
                    print(self.plateau.__str__())
                    print("*******************************************")
                    ok1= self.plateau.est_gagnant(self.joueurs[0].pion)
                    ok2 = self.plateau.est_gagnant(self.joueurs[1].pion)
                    if ((ok1 ==True) or(ok2== True)):
                        break

                if((ok1 == True) and (ok2 == False)):
                    self.joueurs[0].nb_parties_gagnees += 1
                    print("Partie terminée! Le joueur gagnant est: ",self.joueurs[0].nom)
                    print("Parties gagnées par ",self.joueurs[0].nom," : ",self.joueurs[0].nb_parties_gagnees)
                    print("Parties gagnées par ",self.joueurs[1].nom," : ",self.joueurs[1].nb_parties_gagnees)
                    print("Parties nulles: ",self.nb_parties_nulles)
                    rep = input("Voulez-vous recommencer (O,N)? ")
                    while( rep.upper() not in ["O","N"]):
                        print("Valeur Incorrect")
                        rep = input("Voulez-vous recommencer (O,N)? ")


                if((ok1 == False) and (ok2 == True)):
                    self.joueurs[1].nb_parties_gagnees += 1
                    print("Partie terminée! Le joueur gagnant est: ",self.joueurs[1].nom)
                    print("Parties gagnées par ",self.joueurs[0].nom," : ",self.joueurs[0].nb_parties_gagnees)
                    print("Parties gagnées par ",self.joueurs[1].nom," : ",self.joueurs[1].nb_parties_gagnees)
                    print("Parties nulles: ",self.nb_parties_nulles)
                    rep = input("Voulez-vous recommencer (O,N)? ")
                    while( rep.upper() not in ["O","N"]):
                        print("Valeur Incorrect")
                        rep = input("Voulez-vous recommencer (O,N)? ")

                if((ok1 == False) and (ok2 == False)):
                    self.nb_parties_nulles += 1
                    print("Partie terminée! Partie est nulle")
                    print("Parties gagnées par ",self.joueurs[0].nom," : ",self.joueurs[0].nb_parties_gagnees)
                    print("Parties gagnées par ",self.joueurs[1].nom," : ",self.joueurs[1].nb_parties_gagnees)
                    print("Parties nulles: ",self.nb_parties_nulles)
                    rep = input("Voulez-vous recommencer (O,N)? ")
                    while( rep.upper() not in ["O","N"]):
                        print("Valeur Incorrect")
                        rep = input("Voulez-vous recommencer (O,N)? ")





        if(choix == 2):
            print("SVP entrer votre nom : ")
            nom = input()
            print(nom," SVP entrer votre pion : ")
            pion = self.demander_forme_pion()
            joueur1 = Joueur(nom,"Personne",pion)
            self.joueurs.append(joueur1)
            print("Saisir nom de l'autre joueur ")
            nom2 = input()

            if(joueur1.pion == "X"):
                joueur2 = Joueur(nom2,"Personne","O")
                self.joueurs.append(joueur2)
            else:
                joueur2 = Joueur(nom2,"Personne","X")
                self.joueurs.append(joueur2)

            self.joueur_courant = self.joueurs[0]
            rep = ""
            while ( rep.upper() != "N" ):
                self.plateau = Plateau()
                print(self.plateau.__str__())
                while(self.plateau.non_plein()):
                    self.tour(choix)
                    print(self.plateau.__str__())
                    print("*******************************************")
                    ok1= self.plateau.est_gagnant(self.joueurs[0].pion)
                    ok2 = self.plateau.est_gagnant(self.joueurs[1].pion)
                    if((ok1 == True) or(ok2 == True)):
                        break

                if((ok1 == True) and (ok2 == False)):
                    self.joueurs[0].nb_parties_gagnees += 1
                    print("Partie terminée! Le joueur gagnant est: ",self.joueurs[0].nom)
                    print("Parties gagnées par ",self.joueurs[0].nom," : ",self.joueurs[0].nb_parties_gagnees)
                    print("Parties gagnées par ",self.joueurs[1].nom," : ",self.joueurs[1].nb_parties_gagnees)
                    print("Parties nulles: ",self.nb_parties_nulles)
                    rep = input("Voulez-vous recommencer (O,N)? ")
                    while( rep.upper() not in ["O","N"]):
                        print("Valeur Incorrect")
                        rep = input("Voulez-vous recommencer (O,N)? ")


                if((ok1 == False) and (ok2 == True)):
                    self.joueurs[1].nb_parties_gagnees += 1
                    print("Partie terminée! Le joueur gagnant est: ",self.joueurs[0].nom)
                    print("Parties gagnées par ",self.joueurs[0].nom," : ",self.joueurs[0].nb_parties_gagnees)
                    print("Parties gagnées par ",self.joueurs[1].nom," : ",self.joueurs[1].nb_parties_gagnees)
                    print("Parties nulles: ",self.nb_parties_nulles)
                    rep = input("Voulez-vous recommencer (O,N)? ")
                    while( rep.upper() not in ["O","N"]):
                        print("Valeur Incorrect")
                        rep = input("Voulez-vous recommencer (O,N)? ")

                if((ok1 == False) and (ok2 == False)):
                    self.nb_parties_nulles += 1
                    print("Partie terminée! Partie est Nulle")
                    print("Parties gagnées par ",self.joueurs[0].nom," : ",self.joueurs[0].nb_parties_gagnees)
                    print("Parties gagnées par ",self.joueurs[1].nom," : ",self.joueurs[1].nb_parties_gagnees)
                    print("Parties nulles: ",self.nb_parties_nulles)
                    rep = input("Voulez-vous recommencer (O,N)? ")
                    while( rep.upper() not in ["O","N"]):
                        print("Valeur Incorrect")
                        rep = input("Voulez-vous recommencer (O,N)? ")    
                    
                        
                    
        else:


            print("Merci Au revoir")


    def saisir_nombre(self, nb_min, nb_max):
        """
        Permet de demander à l'utilisateur un nombre et doit le valider.
        Ce nombre doit être une valeur entre nb_min et nb_max.
        Vous devez utiliser la méthode isnumeric() afin de vous assurer que l'utilisateur entre
        une valeur numérique et non pas une chaîne de caractères.
        Veuillez consulter l'exemple d'exécution du jeu mentionné dans l'énoncé du TP
        afin de savoir quoi afficher à l'utilisateur.

        Args:
            nb_min (int): Un entier représentant le minimum du nombre à entrer.
            nb_max (int): Un entier représentant le maximum du nombre à entrer.

        Returns:
            int: Le nombre saisi par l'utilisateur après validation.
        """
        assert isinstance(nb_min, int), "Partie: nb_min doit être un entier."
        assert isinstance(nb_max, int), "Partie: nb_max doit être un entier."

        nb = input()

        while((nb.isnumeric() == False) or( int(nb) not in range(nb_min,nb_max))):
            print("******Valeur Incorrecte********")
            nb = input()

        return int(nb)    

        

    def demander_forme_pion(self):
        """
        Permet de demander à l'utilisateur un caractère et doit le valider.
        Ce caractère doit être soit 'O' soit 'X'.
        Veuillez consulter l'exemple d'exécution du jeu mentionné dans l'énoncé du TP
        afin de savoir quoi afficher à l'utilisateur.

        Returns:
            string: Le catactère saisi par l'utilisateur après validation.
        """


        pion  = input()

        while(pion.upper() not in ["O","X"]):
            print("******Valeur Incorrecte********")
            pion  = input()

        return pion.upper()
            
            

    def tour(self, choix):
        """
        Permet d'exécuter le tour d'un joueur (une personne ou un ordinateur).
        Cette méthode doit afficher le plateau (voir la méthode __str__() de la classe Plateau).
        Si le joueur courant est un ordinateur, il faut calculer la position de la prochaine
        case à jouer par cet ordinateur en utilisant la méthode choisir_prochaine_case().
        Si le joueur courant est une personne, il faut lui demander la position de la prochaine
        case qu'il veut jouer en utilisant la méthode demander_postion().
        Finalement, il faut utiliser la méthode selectionner_case() pour modifier le contenu
        de la case choisie soit par l'ordinateur soit par la personne.

        Args:
            choix (int): Un entier représentant le choix de l'utilisateur dans le menu du jeu (1 ou 2).
        """

        assert isinstance(choix, int), "Partie: choix doit être un entier."
        assert choix in [1, 2], "Partie: choix doit être 1 ou 2."

        if ( int(choix) == 1):
            if(self.joueur_courant == self.joueurs[0]):
                    print(self.joueur_courant.nom ," : Entrez s.v.p. les coordonnées de la case à utiliser: ")
                    ligne,colonne = self.demander_position()
                    self.plateau.selectionner_case(ligne,colonne,self.joueur_courant.pion)
                    self.joueur_courant = self.joueurs[1]
            else:
                    ligne,colonne = self.plateau.choisir_prochaine_case(self.joueur_courant.pion)
                    self.plateau.selectionner_case(ligne,colonne,self.joueur_courant.pion)
                    self.joueur_courant = self.joueurs[0]





                    
        else:
            if(self.joueur_courant == self.joueurs[0]):
                print(self.joueur_courant.nom ," : Entrez s.v.p. les coordonnées de la case à utiliser: ")
                ligne,colonne = self.demander_position()
                self.plateau.selectionner_case(ligne,colonne,self.joueur_courant.pion)
                self.joueur_courant = self.joueurs[1]
            else:
                
                print(self.joueur_courant.nom ," : Entrez s.v.p. les coordonnées de la case à utiliser: ")
                ligne,colonne = self.demander_position()
                self.plateau.selectionner_case(ligne,colonne,self.joueur_courant.pion)
                self.joueur_courant = self.joueurs[0]
                    

    def demander_position(self):
        """
        Permet de demander à l'utilisateur les coordonnées de la case qu'il veut jouer.
        Cette méthode doit valider ces coordonnées (ligne,colonne).
        Voici un exemple de ce qu'il faut afficher afin de demander cette position:

        Mondher : Entrez s.v.p. les coordonnées de la case à utiliser:
        Numéro de la ligne:Entrez s.v.p. un nombre entre 0 et 2:? 0
        Numéro de la colonne:Entrez s.v.p. un nombre entre 0 et 2:? 0

        Il faut utiliser la méthode saisir_nombre() et position_valide().

        Returns:
            (int,int):  Une paire d'entiers représentant les
                        coordonnées (ligne, colonne) de la case choisie.
        """
        print("Numéro de la ligne:Entrez s.v.p. un nombre entre 0 et 2:? ")
        ligne = self.saisir_nombre(0,3)
        print("Numéro de la colonne:Entrez s.v.p. un nombre entre 0 et 2:? ")
        colonne = self.saisir_nombre(0,3)

        while(  self.plateau.position_valide(int(ligne),int(colonne)) == False):
            print("Position Occupé")
            print("Numéro de la ligne:Entrez s.v.p. un nombre entre 0 et 2:? ")
            ligne = self.saisir_nombre(0,3)
            print("Numéro de la colonne:Entrez s.v.p. un nombre entre 0 et 2:? ")
            colonne = self.saisir_nombre(0,3)

        return (int(ligne),int(colonne))

            
        

if __name__ == "__main__":
    # Point d'entrée du programme.
    # On initialise une nouvelle partie, et on appelle la méthode jouer().
    partie = Partie()
    partie.jouer()

