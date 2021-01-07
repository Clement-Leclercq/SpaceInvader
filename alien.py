#------------------Classe alien------------------------#
class alien :
    def __init__(self,cType,cPosition,cDurability) :
        self.__type = cType
        self.__position = cPosition
        self.__durability = cDurability

    def setPosition(self,newPosition):
        self.__position = newPosition
        #Place le vaisseau de l'alien avec une méthode .coord

    def getPosition(self):
        return self.__position

    def goingLeft(self):y   
        #Le l'alien va à gauche
        if self.__position[0] > 50 :
            self.setPosition(self.__position[0]-10)

    def goingRight(self):
        #L'alien va à droite 
        if self.__position[0] < 850 :
            self.setPosition(self.__position[0]+10) 
    
    def decreaseDurability(self,decrease):
        self.__durability -= decrease
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
