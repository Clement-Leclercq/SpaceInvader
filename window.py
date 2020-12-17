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
def play():
    print("test")

"""
Création du joueur
"""
score = 0
lives = 3
position = [450,800]

player1 = player(score,lives,position)



"""
Programme gérant la création de la fenêtre
"""
#Création de la fenêtre
spaceWindow = Tk()
spaceWindow.title("Space Invader")
spaceWindow.geometry("980x690+200+100")

#Création des différents éléments
#Les boutons
quitButton = Button(spaceWindow, text = "Quit", command = spaceWindow.destroy)
newButton = Button(spaceWindow, text = "New game", command = play)
#Les label
lives = StringVar ()
lives.set("Lives: "+player.getLife())
score = StringVar ()
score.set("Score:")
livesLabel = Label(spaceWindow, textvariable = lives)
scoreLabel = Label(spaceWindow, textvariable = score)
#Le Canvas => penser à mettre le vaisseau
picture = PhotoImage(file="picture/background.gif")
x = 900
y = 900
spaceCanvas = Canvas(spaceWindow, width = x, height = y)
spaceCanvas.create_image(0,0,anchor=NW, image = picture)

#Agencement dans la fenêtre
scoreLabel.grid(row = 1, column = 1, sticky = W)
livesLabel.grid(row = 1, column = 1, sticky = E)
spaceCanvas.grid(row = 2, column = 1, rowspan = 2)
newButton.grid(row = 2, column = 2)
quitButton.grid(row = 2, column = 2, sticky = S)

spaceWindow.mainloop()





    

#---------Code-----------#

#Fonction qui gère l'input de l'utilisateur pour renvoyer un  :

def playerMove(event,pPlayer) :
    key = event.keysym
    if key == 'KP_Right' : 
        pPlayer.goRight()
    elif key == 'KP_Left' :
        pPlayer.goLeft()
    elif key == 'space' :
        pPlayer.playerShoot()

