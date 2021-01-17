"""
Ce programme crée la classe bunker
Programme fait par Pierre Gosson et Clément Leclercq
Fait le 17/12/2020
TO DO: Complete
"""
#Importation pour placer le bunker#

from tkinter import Tk, Canvas, PhotoImage, NW, W, E, N, S

#------------------Classe bunker(barrière/protection pour le joueur)------------------------#

#Classe bunker contenant la position X (entier) et Y (entier)
#Les fonctions permettent de modifier et retourner ces dernieres, ainsi que d'afficher le bunker dans le canvas.
class bunker :
    def __init__(self,cXPos,cYPos) :
        self.__xPos = cXPos #Entier comportant la position en X sur le canvas de notre bunker
        self.__yPos = cYPos #Entier comportant la position en Y sur le canvas de notre bunker
            
    def setPosition(self,newXPosition,newYPosition):
        #Définie une nouvelle position X et Y pour le bunker
        self.__xPos = newXPosition
        self.__yPos = newYPosition
        

    def getPosition(self):
        #Retourne une liste contenant la position X et Y du bunker
        return [self.__xPos,self.__yPos]

    def dispBunker(self,idCanvas,picture):
        #Permet d'afficher le bunker sur le canvas 
        return idCanvas.create_image(self.__xPos,self.__yPos, image = picture)
        

    























