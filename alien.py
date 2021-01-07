"""
Ce programme crée la classe alien
Programme fait par Pierre Gosson et Clément Leclercq
Fait le 17/12/2020
TO DO: Tout
"""
#------------------Classe alien------------------------#
class alien :
    def __init__(self,cNumber,cPosition) :
        self.__number = cNumber
        self.__position = cPosition

    def setPosition(self,newPosition):
        self.__position = newPosition
        #Place le vaisseau de l'alien avec une méthode .coord

    def getPosition(self):
        return self.__position

    def goingLeft(self):
        #Le l'alien va à gauche
        if self.__position[0] > 0 + self.__shipSize :
            self.setPosition(self.__position[0]-10)

    def goingRight(self):
        #L'alien va à droite 
        if self.__position[0] < 900 - self.__shipSize :
            self.setPosition(self.__position[0]+10) 
"""
    def alienShoot(self):
        #Crée un tir d'alien 

    def bounceToRight(self):
        #Rebond à droite

    def bounceToLeft(self):
        #Rebond à gauche

    def goDown(self):
        #Les aliens descendent lors d'un aller retour donc lors d'un allé retour.
"""
