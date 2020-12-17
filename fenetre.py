# -*- coding: utf-8 -*-

#Header
"""
Ce programme permet la création de la fenêtre
Programme fait par Pierre Gosson et Clément Leclercq
Fait le 17/12/2020
TO DO: 
"""
#------------Classe joueur-----------------#
#Classe joueur qui va nous donner et modifié son score, ses vies
#Qui va aussi lui permettre de tirer et de se déplacer
class player : 
    def __init__(self,cScore,cLife,cPosition) :
        self.__life=cLife
        self.__score=cScore
        self.__position=cPosition


    def setLife(self,newlife):
        self.__life=newlife


    def getLife(self):
        return self.__life

    def setScore(self,newScore):
        self.__score=newScore

    def getScore(self):
        return self.__score

    def playerShoot(self):
        #Faire ici la fonction tkinter ou quand on appui
        #Sur espace ça tire

    def goLeft(self):
        #Le joueur va à gauche 

    def goRight(self):
        #Le joueur va à droite

    def shipSize(self):
        #Taille du vaisseau

    def setPosition(self,newPosition):
        self.__position=newPosition
        #PLace le vaisseau du joueur avec une méthode .coord


    def getPosition(self):
        return self.__position




#------------------Classe alien------------------------#
class alien :
    def __init__(self,cNumber,cPosition) :
        self.__number=cNumber
        self.__position=cPosition

    def setPosition(self,newPosition):
        self.__position=newPosition
        #Place le vaisseau du joueur avec une méthode .coord


    def getPosition(self):
        return self.__position

    def alienShoot(self):
        #Crée un tir d'alien 

    def bounceToRight(self):
        #Rebond à droite

    def bounceToLeft(self):
        #Rebond à gauche

    

#---------Code-----------#

#Une fonction 















