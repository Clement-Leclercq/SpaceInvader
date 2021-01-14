"""
Ce programme crée la classe alien
Programme fait par Pierre Gosson et Clément Leclercq
Fait le 17/12/2020
TO DO: Tout
"""
#------------------Classe alien------------------------#
class alien :
    def __init__(self,cType,cPosition,cDurability,cSpeed = [10,25]) :
        self.__type = cType
        self.__position = cPosition
        self.__durability = cDurability
        self.__speed = cSpeed

    def setPosition(self,newPosition):
        self.__position = newPosition
        #Place le vaisseau de l'alien avec une méthode .coord

    def getPosition(self):
        return self.__position

    def getType(self):
        return self.__type

    def goingDown(self):
        self.__position[1] += self.__speed[1]

    def goingLeft(self):   
        #L'alien va à gauche
        self.__position[0] -= self.__speed[0]

    def goingRight(self):
        #L'alien va à droite 
        self.__position[0] += self.__speed[0] 
    
    def decreaseDurability(self,decrease):
        self.__durability -= decrease
    
    def getDurability(self):
        return self.__durability
    
    def dispAlien(self,idCanvas,picture):
        return idCanvas.create_image(self.__position[0],self.__position[1], image = picture)
    
    def getHitbox(self):
        if self.__type != 3:
            return [30,25]
        else:
            return [55,55]
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
