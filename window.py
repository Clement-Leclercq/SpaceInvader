# -*- coding: utf-8 -*-

#Header
"""
Ce programme permet la création de la fenêtre
Programme fait par Pierre Gosson et Clément Leclercq
Fait le 17/12/2020
TO DO: 
"""
#Imporation de time pour permettre la gestion de pause
import time
from random import randint

#Importation des bibliothèques tkinter nécessaires
from tkinter import Tk, Button, Label, StringVar, Entry, Canvas, PhotoImage, NW, W, E, N, S,Toplevel
from tkinter import messagebox #permet la boite de dialogue

#Importation de nos classes
from player import player #Classe player qui gère vie et score et position du vaisseau
from alien import alien #Classe alien qui gère le nombre et la position de l'alien
from bunker import bunker #Classe bunker qui gère les protections entre le joueur et les aliens

def newPlayer(): #Fonction qui permet de créer un objet de classe joueur avec des paramètres standards (score de 0 / 3 vies / position de base)
    return player(0,3,[450,700])

def newGame():
    global alienIdList,alienList,bunkerList,idBunkerList
    for element in alienIdList:
        spaceCanvas.delete(element)
    for element in idBunkerList:
        spaceCanvas.delete(element)
    alienIdList = []
    alienList = []
    bunkerList = []
    idBunkerList = []
    play()
#Fonction qui permet d'instancier le player1 et d'obtenir les paramètres Vie / Score / position et de les afficher
def play():
    global lives,score,player1
    player1 = newPlayer()
    spaceCanvas.coords(shipId,player1.getPosition()[0],player1.getPosition()[1])
    lives.set("Lives: "+str(player1.getLife()))
    score.set("Score: "+str(player1.getScore()))
    spaceCanvas.focus_set()
    bunkers()
    aliens()
    boss()

#Fonction qui gère l'input de l'utilisateur pour gérer son tir ou son déplacement
def playerMove(event,pPlayer) :
    global shoot
    key = event.keysym
    if key == 'Right' : 
        pPlayer.goRight()
    elif key == 'Left' :
        pPlayer.goLeft()
    elif key == 'space' and shoot == False:
        playerShoot()
    spaceCanvas.coords(shipId,pPlayer.getPosition()[0],pPlayer.getPosition()[1])

#Fonction qui gère le tir du joueur
def playerShoot():
    global shoot
    def _shootMove(X,Y): #Fonction interne 
        global shoot
        global alienList
        global alienIdList

        posList = []
        for element in alienList:
            posList.append(element.getPosition())
        alienTouch = False
        for i,element in enumerate(posList):
            hitbox = alienList[0].getHitbox()
            if X > element[0]-hitbox[0] and X < element[0]+hitbox[0] and Y > element[1]-hitbox[1] and Y < element[1]+hitbox[1]:
                print(i)
                alienList[i].decreaseDurability(1)
                if alienList[i].getDurability() == 0:
                    spaceCanvas.delete(alienIdList[i])
                    alienIdList.pop(i)
                    alienList.pop(i)
                spaceCanvas.delete(vaccineId)
                alienTouch = True
                shoot = False
        if Y < 50 and alienTouch == False:
            spaceCanvas.delete(vaccineId)
            shoot = False
        elif alienTouch == False:
            Y -= 25
            spaceCanvas.coords(vaccineId,X,Y)
            spaceWindow.after(50,_shootMove,X,Y)
    shoot = True
    positionX = player1.getPosition()[0]
    positionY = player1.getPosition()[1] - 50
    vaccineId = spaceCanvas.create_image(positionX,positionY,image = vaccine)
    spaceWindow.after(50,_shootMove,positionX,positionY)
    

#Fonction qui crée la liste de bunker avec son image dans le canvas
def bunkerCreate(fXPos,fYPos,fNbrBunker) :
    global idBunkerList
    global bunkerList
    for i in range (0,fNbrBunker) :    
        tempBunker = bunker(fXPos,fYPos)
        bunkerList.append(tempBunker)
        idBunkerList.append(tempBunker.dispBunker(spaceCanvas,imBunker))
        fXPos += 50


#Fonction qui positionne les bunkers :
def bunkers() :
    global idBunkerList
    global bunkerList
#Premiere ligne 
    bunkerCreate(25,600,3)
    bunkerCreate(275,600,3)
    bunkerCreate(525,600,3)
    bunkerCreate(775,600,3)
#Deuxième ligne
    bunkerCreate(25,550,3)
    bunkerCreate(275,550,3)
    bunkerCreate(525,550,3)
    bunkerCreate(775,550,3)

    
#Fonction qui positionne les aliens :
def alienCreate(xPos,yPos,nbr,nbrKaren):
    global alienList
    global alienIdList
    alienType = 1
    for i in range(0,nbr):
        tempAlien = alien(alienType,[xPos,yPos],1)
        alienList.append(tempAlien)
        if nbrKaren > 0:
            if alienType == 1:
                image = covid
                alienType = 2
            else:
                image = karen
                alienType = 1
            alienIdList.append(tempAlien.dispAlien(spaceCanvas,image))
            xPos += 60
        else:
            image = covid
            alienIdList.append(tempAlien.dispAlien(spaceCanvas,image))
            xPos += 60


def alienShoot(fAlien,alienList) :
    time = randint(7000,10000)
    def _Shoot(X,Y,alienList) :
        test = False
        if Y > 850 :
            spaceCanvas.delete(covideProjectileId)
            if fAlien in alienList:
                spaceWindow.after(time,alienShoot,fAlien,alienList)
        else:
            Y += 25
            spaceCanvas.coords(covideProjectileId,X,Y)
            spaceWindow.after(50,_Shoot,X,Y,alienList)
    
    if fAlien in alienList:
        positionX = fAlien.getPosition()[0] 
        positionY = fAlien.getPosition()[1] + 38
        covideProjectileId = spaceCanvas.create_image(positionX,positionY,image = covidProjectile)
        spaceWindow.after(50,_Shoot,positionX,positionY,alienList)
        


#Fonction qui positionne les aliens : 
def aliens():
    global alienList
    global alienIdList
    move = 1
    alienCreate(75,50,11,5)
    alienCreate(100,110,11,0)
    alienCreate(75,170,11,0)
    alienCreate(100,230,11,5)
    alienMove(alienList,alienIdList,move)
    for element in alienList:
        if element.getType() == 2:
            time = randint(7000,10000)
            spaceWindow.after(time,alienShoot,element,alienList)

def boss():
    global alienList
    global alienIdList

    if alienList != []:
        spaceWindow.after(1000,boss)
    else:
        tempBoss = alien(3,[450,50],5,[50,50])
        alienList.append(tempBoss)
        alienIdList.append(tempBoss.dispAlien(spaceCanvas,trump))
        alienMove(alienList,alienIdList,1)
        time = randint(5000,7000)
        spaceWindow.after(time,alienShoot,tempBoss,alienList)

#Fonction qui gère le déplacement des aliens (pour l'instant que des allées retours) :
def alienMove(alienList,alienIdList,move):
    if len(alienList)>0:
        posAlienLeft = alienList[0].getPosition()
        posAlienRight = alienList[-1].getPosition()
        for element in alienList:
            posAlien = element.getPosition()
            if posAlien[0] < posAlienLeft[0]:
                posAlienLeft = posAlien
            elif posAlien[0] > posAlienRight[0]:
                posAlienRight = posAlien
        hitbox = alienList[0].getHitbox()
        if posAlienLeft[0] > hitbox[0] and move == 0:
            for element,idElement in zip(alienList,alienIdList):
                element.goingLeft()
                changingCoord(element,idElement)
            spaceWindow.after(200,alienMove,alienList,alienIdList,move)
        elif posAlienLeft[0] <= hitbox[0] and move == 0:
            move = 1
            for element,idElement in zip(alienList,alienIdList):
                element.goingDown()
                changingCoord(element,idElement)
            spaceWindow.after(200,alienMove,alienList,alienIdList,move)
        elif posAlienRight[0] < 900-hitbox[0] and move == 1:
            for element,idElement in zip(alienList,alienIdList):
                element.goingRight()
                changingCoord(element,idElement)
            spaceWindow.after(200,alienMove,alienList,alienIdList,move)
        else :
            move = 0
            spaceWindow.after(200,alienMove,alienList,alienIdList,move)

def changingCoord(tempAlien,idAlien):
    spaceCanvas.coords(idAlien,tempAlien.getPosition()[0],tempAlien.getPosition()[1])


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
newButton = Button(spaceWindow, text = "New game", command = newGame)
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

#Image et variables globales
player1 = newPlayer()
bunkerList = []
idBunkerList = []
alienList = []
alienIdList = []
vaccine = PhotoImage(file = "picture/playershoot.gif")
covidProjectile = PhotoImage(file="picture/covidProjectile.gif")
shoot = False
imBunker = PhotoImage(file = "picture/masqueCovid.gif")
ship = PhotoImage(file = "picture/harold.gif")
covid = PhotoImage(file = "picture/covid1.gif")
karen = PhotoImage(file = "picture/karen.gif")
trump = PhotoImage(file = "picture/trump.gif")

#Création du vaisseau  et de ses intéractions
shipId = spaceCanvas.create_image(0,0,image = ship)
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
haroldAskForHelp.attributes("-topmost",True)
spaceWindow.mainloop()





