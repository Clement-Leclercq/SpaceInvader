"""
Ce programme crée la classe alien
Programme fait par Pierre Gosson et Clément Leclercq
Fait le 17/12/2020
TO DO: Complete
"""
#------------------Classe alien------------------------#
#Classe alien possédant un type (entier), une position (liste), une durabilité (entier), une vitesse(liste)
#Les fonctions permettent de retourner ces composants et de les modifier. Egalement de faire apparaitre l'alien sur le canvas
#Et de le faire bouger (horizontalement,verticalement)
class alien :
    def __init__(self,cType,cPosition,cDurability,cSpeed = [10,25]) :
        self.__type = cType #Un entier entre 1 et 3 donnant le type d'alien dans le jeu
        self.__position = cPosition #Liste donnant la position en X (en premier) et en Y (en deuxieme)
        self.__durability = cDurability #Un entier donnant la vie de l'alien 
        self.__speed = cSpeed #Une liste donnant la vitesse selon X et Y de la forme (speedX,speedY)

    def setPosition(self,newPosition):
        #Définie avec une nouvelle liste (X,Y) la nouvelle position de l'alien
        self.__position = newPosition
        

    def getPosition(self):
        #Retourne la liste (X,Y) de la position de l'alien
        return self.__position
        

    def getType(self):
        #Retourne l'entier définissant le type de l'alien
        return self.__type
        

    def goingDown(self):
        #Permet de faire descendre l'alien
        self.__position[1] += self.__speed[1]
        
    def goingLeft(self):   
        #L'alien va à gauche
        self.__position[0] -= self.__speed[0]

    def goingRight(self):
        #L'alien va à droite 
        self.__position[0] += self.__speed[0] 
    
    def decreaseDurability(self,decrease):
        #Baisse de la variable decrease la durabilité (vie) de l'alien
        self.__durability -= decrease
        
    
    def getDurability(self):
        #Retourne la vie de l'alien
        return self.__durability
    
    def dispAlien(self,idCanvas,picture):
        #Permet d'afficher l'alien dans le canvas 
        return idCanvas.create_image(self.__position[0],self.__position[1], image = picture)
    
    def getHitbox(self):
        #Retourne la hitbox des aliens selon leur type (différenciation alien normaux et boss)
        if self.__type != 3:
            return [30,25]
        else:
            return [55,55]

