# -*- coding: utf-8 -*-

#Header
"""
Ce programme permet la création de la fenêtre
Programme fait par Pierre Gosson et Clément Leclercq
Fait le 17/12/2020
TO DO: Tout
"""

#Importation des bibliothèques tkinter nécessaires
from tkinter import Tk, Button, Label, StringVar, Entry, Canvas, PhotoImage, NW, W, E, N, S
from tkinter import messagebox #permet la boite de dialogue

#Importation de nos classes
from player import player #Classe player qui gère vie et score et position du vaisseau
from alien import alien #Classe alien qui gère le nombre et la position de l'alien

def newPlayer(): #Fonction qui permet de créer un objet de classe joueur avec des paramètres standards (score de 0 / 3 vies / position de base)
    return player(0,3,[450,850])

def play():
    global lives,score,player1
    player1 = newPlayer()
    lives.set("Lives: "+str(player1.getLife()))
    score.set("Score: "+str(player1.getScore()))
"""
Programme gérant la création de la fenêtre avec son initialisation
"""
#Création de la fenêtre
spaceWindow = Tk()
spaceWindow.title("Space Covid Invader Ultimate Edition")
spaceWindow.geometry("980x930+0+0")
#Création des différents éléments
#Les boutons
quitButton = Button(spaceWindow, text = "Quit", command = spaceWindow.destroy)
newButton = Button(spaceWindow, text = "New game", command = play)
#Les label
lives = StringVar ()
lives.set("Lives: ")
score = StringVar ()
score.set("Score: 0")
livesLabel = Label(spaceWindow, textvariable = lives)
scoreLabel = Label(spaceWindow, textvariable = score)
#Le Canvas
picture = PhotoImage(file="picture/covidBackground.gif")
x = 900
y = 900
spaceCanvas = Canvas(spaceWindow, width = x, height = y)
spaceCanvas.create_image(0,0,anchor=NW, image = picture)

ship = PhotoImage(file = "picture/harold.gif")
spaceCanvas.create_image(450,850,image = ship)
spaceCanvas.focus_set()
spaceCanvas.bind("KP_Right",lambda event,player1 : playerMove)
spaceCanvas.bind("KP_Left",lambda event,player1 : playerMove)
spaceCanvas.bind("space",lambda event,player1 : playerMove)

#Agencement dans la fenêtre
scoreLabel.grid(row = 1, column = 1, sticky = W)
livesLabel.grid(row = 1, column = 1, sticky = E)
spaceCanvas.grid(row = 2, column = 1, rowspan = 2)
newButton.grid(row = 2, column = 2)
quitButton.grid(row = 2, column = 2, sticky = S)

play()

spaceWindow.mainloop()

#---------Code-----------#

#Fonction qui gère l'input de l'utilisateur pour renvoyer un  :

def playerMove(event,pPlayer) :
    key = event.keysym
    if key == 'KP_Right' : 
        pPlayer.goRight()
        print("droite")
    elif key == 'KP_Left' :
        pPlayer.goLeft()
        print("gauche")
    elif key == 'space' :
        pPlayer.playerShoot()
        print("espace")
    spaceCanvas.coords(ship,pPlayer.getPosition(0),pPlayer.getPostition(1))


#Fonction qui gère le déplacement des aliens (pour l'instant que des allées retours) :

def alienMove() :
    
