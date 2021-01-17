"""
Ce programme crée la classe player
Programme fait par Pierre Gosson et Clément Leclercq
Fait le 17/12/2020
TO DO: Complete
"""
#------------Classe joueur-----------------#
#Classe joueur qui va nous donner et modifié son score(entier), ses vies(entier), ainsi que sa position(liste)
#Qui va aussi lui permettre de tirer et de se déplacer
class player : 
    def __init__(self,cScore,cLife,cPosition=[0,0]) :
        self.__life = cLife #Entier donnant le nombre de vie restante au joueur
        self.__score = cScore #Entier donnant le score du joueur (il augmente et descend au cours du jeu)
        self.__position = cPosition #Liste (X,Y) donnant la position du joueur 
        self.__shipSize = 50 #Entier donnant la taille du vaisseau du joueur

    def setLife(self,newlife):
        # Fonction permettant de donner un nouvel entier caractérisant le nombre de vie du joueur
        self.__life = newlife
    
    def decreaseLife(self):
        #Fonction qui diminue l'entier vie 
        self.__life -= 1

    def getLife(self):
        #Retourne le nombre de vie du joueur
        return self.__life

    def setScore(self,newScore):
        #Donne un nouveau entier à la variable score
        self.__score = newScore

    def decreaseScore(self):
        #Baisse le score du joueur
        self.__score -= 50

    def increaseScore(self,point):
        #Augmente le score du joueur
        self.__score += point

    def getScore(self):
        #Retourne le score du joueur
        return self.__score

    def goRight(self):
        #Le joueur va à droite 
        if self.__position[0] < 850:
            self.setPositionX(self.__position[0]+10) 

    def goLeft(self):
        #Le joueur va à gauche
        if self.__position[0] > 50 :
            self.setPositionX(self.__position[0]-10)

    def setPositionX(self,newPosition):
        #Définie une nouvelle position pour le joueur 
        self.__position[0] = newPosition
        

    def getPosition(self):
        #Retourne la position du joueur
        return self.__position


