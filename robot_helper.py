import tkinter as tk
import random
import math
import tkinter as tk
import numpy as np
class Charger:
    def __init__(self,namep):
        self.centreX = random.randint(100,900)
        self.centreY = random.randint(100,900)
        self.name = namep

    def draw(self,canvas):
        body = canvas.create_oval(self.centreX-10,self.centreY-10, \
                                  self.centreX+10,self.centreY+10, \
                                  fill="gold",tags=self.name)

    def getLocation(self):
        return self.centreX, self.centreY

class WiFiHub:
    def __init__(self,namep,xp,yp):
        self.centreX = xp
        self.centreY = yp
        self.name = namep

    def draw(self,canvas):
        body = canvas.create_oval(self.centreX-10,self.centreY-10, \
                                  self.centreX+10,self.centreY+10, \
                                  fill="purple",tags=self.name)

    def getLocation(self):
        return self.centreX, self.centreY

def initialise(window):
    window.resizable(False,False)
    canvas = tk.Canvas(window,width=1000,height=1000)
    canvas.pack()
    return canvas

def buttonClicked(x,y,registryActives,Bot):
    '''
    Bot is a class
    :param x:
    :param y:
    :param registryActives:
    :param Bot:
    :return:
    '''
    for rr in registryActives:
        if isinstance(rr,Bot):
            rr.x = x
            rr.y = y