"""
Ce programme crée la classe bunker
Programme fait par Pierre Gosson et Clément Leclercq
Fait le 17/12/2020
TO DO: Tout
"""
#Importation pour placer le bunker#

from tkinter import Tk, Canvas, PhotoImage, NW, W, E, N, S

#------------------Classe bunker------------------------#
class bunker :
    def __init__(self,cXPos,cYPos) :
        self.__xPos = cXPos
        self.__yPos = cYPos
        
        
    def setPosition(self,newXPosition,newYPosition):
        self.__xPos = newXPosition
        self.__yPos = newYPosition
        #Place le bunker avec une méthode .coord

    def dispBunker(self,id,picture):
        return id.create_image(self.__xPos,self.__yPos, image = picture)
        

    























