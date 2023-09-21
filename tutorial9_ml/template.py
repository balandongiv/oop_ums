'''
This is working file

'''


import random
import sys
import tkinter as tk

from dynamic_component import Cat
from dynmic_comp import movingCat
from mybot import Bot
from passive_component import Dirt, Counter, WiFiHub, Charger
from robot_helper import initialise

gg=1
def buttonClicked(x,y,registryActives):
    for rr in registryActives:
        if isinstance(rr,Bot):
            rr.x = x
            rr.y = y


def register(canvas):

    registryActives = []
    registryPassives = []
    noOfBots = 1
    noOfCats = 10
    noOfDirt = 300

    for i in range(0,noOfBots):
        bot = Bot("Bot"+str(i),canvas)
        registryActives.append(bot)
        bot.draw(canvas)
    for i in range(0,noOfCats):
        cat = Cat("Cat"+str(i),canvas)
        registryActives.append(cat)
        cat.draw(canvas)
    charger = Charger("Charger")
    registryPassives.append(charger)
    charger.draw(canvas)
    hub1 = WiFiHub("Hub1",950,50)
    registryPassives.append(hub1)
    hub1.draw(canvas)
    hub2 = WiFiHub("Hub2",50,500)
    registryPassives.append(hub2)
    hub2.draw(canvas)
    hub3 = WiFiHub("Hub3",600,800)
    registryPassives.append(hub3)
    hub3.draw(canvas)
    for i in range(0,noOfDirt):
        dirt = Dirt("Dirt"+str(i))
        registryPassives.append(dirt)
        dirt.draw(canvas)
    count = Counter(canvas)
    canvas.bind( "<Button-1>", lambda event: buttonClicked(event.x,event.y,registryActives) )
    return registryActives, registryPassives, count

def moveIt(canvas,registryActives,registryPassives,count,moves,signalStrengths):
    moves += 1
    for rr in registryActives:

        if isinstance(rr,Bot):
            rr=movingCat(rr)
            rr.look(registryActives)
            chargerIntensityL, chargerIntensityR = rr.senseCharger(registryPassives)
            rr.transferFunction(chargerIntensityL, chargerIntensityR)

        if isinstance(rr,Cat):
            rr.transferFunction()

        rr.move(canvas,registryPassives,1.0)
        if isinstance(rr,movingCat):
            registryPassives = rr.collectDirt(canvas,registryPassives, count)
            collision = rr.collision(registryActives)


        numberOfMoves = 100
        print("total dirt collected in",numberOfMoves,"moves is",count.dirtCollected)
        if moves>numberOfMoves:
            print("total dirt collected in",numberOfMoves,"moves is",count.dirtCollected)
            sys.exit()
    canvas.after(50,moveIt,canvas,registryActives,registryPassives,count,moves,signalStrengths)

def training(registryActives, registryPassives,canvas):
    print("training")
    rr = registryActives[0]
    signalStrengths = []
    rr=movingCat(rr)
    for x in range(1):
        for y in range(1):
            topCornerX = x*100.0
            topCornerY = y*100.0
            for _ in range(5):
                positionX = topCornerX + random.uniform(0.0,99.99)
                positionY = topCornerY + random.uniform(0.0,99.99)
                rr.pickUpAndPutDown(positionX,positionY)
                signalStrengths.append( (rr.senseHubs(registryPassives),x,y) )
                # canvas.update()
                # time.sleep(0.1)

    print("Training Completed")
    return signalStrengths
                

def main():
    window = tk.Tk()
    canvas = initialise(window)
    registryActives, registryPassives, count = register(canvas)

    signalStrengths = training(registryActives, registryPassives,canvas)
    
    moves = 0
    moveIt(canvas,registryActives,registryPassives, count, moves, signalStrengths)
    window.mainloop()

main()
