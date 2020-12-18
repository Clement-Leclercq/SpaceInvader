# -*- coding: utf-8 -*-

#Header
"""
Ce programme permet la création de la fenêtre
Programme fait par Pierre Gosson et Clément Leclercq
Fait le 17/12/2020
TO DO: Tout
"""

#Importation des bibliothèques tkinter nécessaires
from tkinter import Tk, Button, Label, StringVar, Entry, Canvas, PhotoImage, NW, W, E, N, S,Toplevel
from tkinter import messagebox #permet la boite de dialogue

#Importation de nos classes
from player import player #Classe player qui gère vie et score et position du vaisseau
from alien import alien #Classe alien qui gère le nombre et la position de l'alien

def newPlayer(): #Fonction qui permet de créer un objet de classe joueur avec des paramètres standards (score de 0 / 3 vies / position de base)
    return player(0,3,[450,700])

def play():
    global lives,score,player1
    player1 = newPlayer()
    spaceCanvas.coords(shipId,pPlayer.getPosition()[0],pPlayer.getPosition()[1])
    lives.set("Lives: "+str(player1.getLife()))
    score.set("Score: "+str(player1.getScore()))
    spaceCanvas.focus_set()

#Fonction qui gère l'input de l'utilisateur pour renvoyer un  :
def playerMove(event,pPlayer) :
    key = event.keysym
    if key == 'Right' : 
        pPlayer.goRight()
    elif key == 'Left' :
        pPlayer.goLeft()
    elif key == 'space' :
        pPlayer.playerShoot()
    spaceCanvas.coords(shipId,pPlayer.getPosition()[0],pPlayer.getPosition()[1])




"""
Programme gérant la création de la fenêtre avec son initialisation
"""
#Création de la fenêtre
spaceWindow = Tk()
spaceWindow.title("Space Covid Invader Ultimate Edition")
spaceWindow.geometry("980x800+0+0")
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
y = 750
spaceCanvas = Canvas(spaceWindow, width = x, height = y)
spaceCanvas.create_image(0,0,anchor=NW, image = picture)

ship = PhotoImage(file = "picture/harold.gif")
shipId = spaceCanvas.create_image(450,700,image = ship)
spaceCanvas.focus_set()
spaceCanvas.bind("<Left>",lambda event : playerMove(event,player1))
spaceCanvas.bind("<Right>",lambda event : playerMove(event,player1))
spaceCanvas.bind("<space>",lambda event : playerMove(event,player1))
#Agencement dans la fenêtre
scoreLabel.grid(row = 1, column = 1, sticky = W)
livesLabel.grid(row = 1, column = 1, sticky = E)
spaceCanvas.grid(row = 2, column = 1, rowspan = 2)
newButton.grid(row = 2, column = 2)
quitButton.grid(row = 2, column = 2, sticky = S)

play()

#Création d'une fenêtre Top level pour présenter le jeu
haroldAskForHelp = Toplevel(spaceWindow)
harold = PhotoImage(file="picture/harold.gif")
haroldLabel = Label(haroldAskForHelp,image = harold)
textLabel = Label(haroldAskForHelp,text = "Oh no Harold is in trouble, Covid-19 is coming for him !\n Make sure he doesn't get Covid 19 thanks to Pfizer's vaccine !\n Harold is counting on you !")
stopButton = Button(haroldAskForHelp, text = "Yes Captain !", command = haroldAskForHelp.destroy)
haroldLabel.grid(row = 1)
textLabel.grid(row = 2)
stopButton.grid(row = 3)
spaceWindow.mainloop()


#Fonction qui gère le déplacement des aliens (pour l'instant que des allées retours) :

def alienMove() :
    print("test")
