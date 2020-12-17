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