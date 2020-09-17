__authors__ = "boutheyna salah & khouloud sadghiani FIA1 Go1"
__date__ = "09/12/2018"

"""
Ce fichier permet de définir la classe plateau du jeu Tic-Tac-Toe.
"""

from case import Case
from random import randrange

class Plateau:
    """
    Classe modélisant le plateau du jeu Tic-Tac-Toe.

    Attributes:
        cases (dictionary): Dictionnaire de cases. La clé est une position (ligne, colonne),
                            et la valeur est une instance de la classe Case.
    """

    def __init__(self):
        """
        Méthode spéciale initialisant un nouveau plateau contenant les 9 cases du jeu.
        """

        # Dictionnaire de cases.
        # La clé est une position (ligne, colonne), et la valeur est une instance de la classe Case.
        self.cases = {}

        # Appel d'une méthode qui initialise un plateau contenant des cases vides.
        self.initialiser()

    def initialiser(self):
        """
        Méthode fournie permettant d'initialiser le plateau avec des cases vides (contenant des espaces).
        """

        # Vider le dictionnaire (pratique si on veut recommencer le jeu).
        self.cases.clear()
        # Parcourir le dictionnaire et mettre des objets de la classe Case.
        # dont l'attribut "contenu" serait un espace (" ").
        for i in range(0, 3):
            for j in range(0, 3):
                self.cases[i,j] = Case(" ")

    def __str__(self):
        """Méthode spéciale fournie indiquant à Python comment représenter une instance de Plateau
        sous la forme d'une chaîne de caractères. Permet donc d'afficher le plateau du jeu
        à l'écran en faisant par exemple:
        p1 = Plateau()
        print(p1)
        Donc, lorsque vous affichez un objet, Python invoque automatiquement la méthode __str__
        Voici un exemple d'affichage:
         +-0-+-1-+-2-+
        0|   | X | X |
         +---+---+---+
        1| O | O | X |
         +---+---+---+
        2|   |   | O |
         +---+---+---+

        Returns:
            string: Retourne la chaîne de caractères à afficher.
        """
        s = " +-0-+-1-+-2-+\n"
        for i in range(0, 3):
            s += str(i)+ "| "
            for j in range(0, 3):
                s += self.cases[(i,j)].contenu + " | "
            if i<=1:
                s += "\n +---+---+---+\n"
            else:
                s += "\n +---+---+---+"
        return s

    def non_plein(self):
        vide = 0
        for i in range(0, 3):
            for j in range(0, 3):
                if self.cases[(i,j)].contenu==" ":
                    vide += 1

        return (vide>0)   
        """
        Retourne si le plateau n'est pas encore plein.
        Il y a donc encore des cases vides (contenant des espaces et non des "X" ou des "O").

        Returns:
            bool: True si le plateau n'est pas plein, False autrement.
        """
       
    def position_valide(self, ligne, colonne):

       
        """
        Vérifie si une position est valide pour jouer.
        La position ne doit pas être occupée.
        Il faut utiliser la méthode est_vide() de la classe Case.

        Args:
            ligne (int): Le numéro de la ligne dans le plateau du jeu.
            colonne (int): Le numéro de la colonne dans le plateau du jeu.

        Returns:
            bool: True si la position est valide, False autrement.
        """
        assert isinstance(ligne, int), "Plateau: ligne doit être un entier."
        assert isinstance(colonne, int), "Plateau: colonne doit être un entier."
        return self.cases[(int(ligne),int(colonne))].est_vide()
     
    def selectionner_case(self, ligne, colonne, pion):
        """
        Permet de modifier le contenu de la case
        qui a les coordonnées (ligne,colonne) dans le plateau du jeu
        en utilisant la valeur de la variable pion.

        Args:
            ligne (int): Le numéro de la ligne dans le plateau du jeu.
            colonne (int): Le numéro de la colonne dans le plateau du jeu.
            pion (string): Une chaîne de caractères ("X" ou "O").
        """
        assert isinstance(ligne, int), "Plateau: ligne doit être un entier."
        assert isinstance(colonne, int), "Plateau: colonne doit être un entier."
        assert isinstance(pion, str), "Plateau: pion doit être une chaîne de caractères."
        assert pion in ["O", "X"], "Plateau: pion doit être 'O' ou 'X'."
        self.cases[(int(ligne),int(colonne))].contenu=pion
        
    def est_gagnant(self, pion):
        
        """
        Permet de vérifier si un joueur a gagné le jeu.
        Il faut vérifier toutes les lignes, colonnes et diagonales du plateau.

        Args:
            pion (string): La forme du pion utilisé par le joueur en question ("X" ou "O").

        Returns:
            bool: True si le joueur a gagné, False autrement.
        """

        assert isinstance(pion, str), "Plateau: pion doit être une chaîne de caractères."
        assert pion in ["O", "X"], "Plateau: pion doit être 'O' ou 'X'."
        ok=False
        trouve=0                  
        for i in range(0,3):
           for j in range(0,3):
              if(self.cases[(i,j)].est_pion(pion)):
                trouve+=1
           if(trouve==3):
              ok=True
              break
           else:
              trouve=0
        if(ok==False):
             for j in range(0,3):
                 for i in range(0,3):
                     if(self.cases[(i,j)].est_pion(pion)):
                        trouve+=1   
                 if(trouve==3):
                     ok=True
                     break
                 else:
                     trouve=0 
        if(ok==False):
            i=0
            j=0
            while((i<3) and (j<3)):
               if(self.cases[(i,j)].est_pion(pion)):
                      trouve+=1
               j+=1
               i+=1
            if(trouve==3):
                  ok=True
            else:
              trouve=0
        if(ok==False):
            i=0
            j=2
            while((i<3) and (j>=0)):
                 if(self.cases[(i,j)].est_pion(pion)):
                      trouve+=1
                 j-=1
                 i+=1    
            if(trouve==3):
              ok=True
        return ok
    def operation(self,pion):
        ok=False
        plein=0
        vide=0
        ligne=-1
        colonne=-1
        for i in range(0,3):
            for j in range (0,3):
                if self.cases[(i,j)].est_pion(pion):
                    plein+=1
                if self.cases[(i,j)].est_vide():
                    vide+=1
                    ligne = i
                    colonne = j
            if (plein==2) and (vide==1):
                
                ok=True
                break
            else:
                plein=0
                vide=0

                
        if (ok==False):
           
            for i in range (0,3):
                for j in range (0,3):
                    if self.cases[(j,i)].est_pion(pion):
                        plein+=1
                    if self.cases[(j,i)].est_vide():
                        
                        vide+=1
                        ligne=j
                        colonne=i
                if (plein==2) and (vide==1):
                    ok=True
                    break
                else:
                    plein=0
                    vide=0
        if (ok==False):
            
            i=0
            j=0
            while (i<=2) and (j<=2):
                if self.cases[(i,j)].est_pion(pion):
                    plein+=1
                    
                if self.cases[(i,j)].est_vide():
                    vide+=1
                    ligne=i
                    colonne=j

                i+=1
                j+=1
            if (plein==2) and (vide==1):
                ok=True
            else:
                vide=0
                plein=0
        if (ok==False):
            
            i=0
            j=2
            while (i<=2) and (j>=0):
                if self.cases[(i,j)].est_pion(pion):
                    plein+=1
                    
                if self.cases[(i,j)].est_vide():
                    vide+=1
                    ligne=i
                    colonne=j

                i+=1
                j-=1
            if (plein==2) and (vide==1):
                
                ok=True
            else:
                vide=0
                plein=0
                ligne=-1
                colonne=-1
        
        return (ligne,colonne)
        
    

    def choisir_prochaine_case(self, pion):
        """
        Permet de retourner les coordonnées (ligne, colonne) de la case que l'ordinateur
        peut choisir afin de jouer contre un autre joueur qui est normalement une personne.
        Ce choix doit se faire en fonction de la configuration actuelle du plateau.
        L'algorithme que vous allez concevoir permettant de faire jouer l'ordinateur
        n'a pas besoin d'être optimal. Cela permettra à l'adversaire de gagner de temps en temps.
        Il faut par contre essayer de mettre le pion de l'ordinateur dans une ligne, une colonne
        ou une diagonale contenant deux pions de l'adversaire pour que ce dernier ne gagne pas facilement.
        Il faut aussi essayer de mettre le pion de l'ordinateur dans une ligne, une colonne
        ou une diagonale contenant deux pions de l'ordinateur pour que ce dernier puisse gagner.
        Vous pouvez utiliser ici la fonction randrange() du module random.
        Par exemple: randrange(1,10) vous retourne une valeur entre 1 et 9 au hasard.

        Args:
            pion (string): La forme du pion de l'adversaire de l'ordinateur ("X" ou "O").

        Returns:
            (int,int): Une paire d'entiers représentant les coordonnées de la case choisie.
        """
        assert isinstance(pion, str), "Plateau: pion doit être une chaîne de caractères."
        assert pion in ["O", "X"], "Plateau: pion doit être 'O' ou 'X'."
        i =-1
        j =-1
        ligne,colonne = self.operation(pion)
        
        if((ligne != -1 ) and (colonne != -1 )):
            i=ligne
            j=colonne
            
        else:
            if(pion == "O"):
                ligne,colonne = self.operation("X")
                if((ligne != -1 ) and (colonne != -1 )):
                     i=ligne
                     j=colonne
               
            if(pion =="X"):
                                   
                ligne,colonne = self.operation("O")
                if((ligne != -1 ) and (colonne != -1 )):
                    i=ligne
                    j=colonne

        if((i==-1) and (j==-1)):
             i= randrange(0,3)
             j= randrange(0,3)
             while(self.position_valide(i,j) == False):
                 i= randrange(0,3)
                 j= randrange(0,3)


        return (i,j)        
            
            
    
