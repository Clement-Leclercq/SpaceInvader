
#------------Classe joueur-----------------#
#Classe joueur qui va nous donner et modifié son score, ses vies
#Qui va aussi lui permettre de tirer et de se déplacer
class player : 
    def __init__(self,cScore,cLife,cPosition=[0,0]) :
        self.__life = cLife
        self.__score = cScore
        self.__position = cPosition
        self.__shipSize = 50

    def setLife(self,newlife):
        self.__life = newlife


    def getLife(self):
        return self.__life

    def setScore(self,newScore):
        self.__score = newScore

    def getScore(self):
        return self.__score

    #def playerShoot(self):
        #Faire ici la fonction tkinter ou quand on appui
        #Sur espace ça tire

    def goRight(self):
        #Le joueur va à droite 
        if self.__position[0] < 850:
            self.setPositionX(self.__position[0]+10) 

    def goLeft(self):
        #Le joueur va à gauche
        if self.__position[0] > 50 :
            self.setPositionX(self.__position[0]-10)

    def setPositionX(self,newPosition):
        self.__position[0] = newPosition
        #PLace le vaisseau du joueur avec une méthode .coord


    def getPosition(self):
        return self.__position


