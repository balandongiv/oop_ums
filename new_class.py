from playsound import playsound
from PIL import Image, ImageTk
import time
import tkinter as tk
import random
import math
import numpy as np
import sys
from passive_component import Dirt,Counter, WiFiHub, Charger
from robot_helper import initialise

from dynamic_component import Cat
class movingCat:
    def __init__(self,robot_obj):
        # self.x = robot_obj.x
        # self.y = robot_obj.y
        # self.theta = robot_obj.theta
        # #self.theta = 0
        # self.name = robot_obj.name
        # self.ll = robot_obj.ll #axle width
        # self.vl = robot_obj.vl
        # self.vr = robot_obj.vr
        # self.battery = robot_obj.battery
        # self.turning = robot_obj.turning
        # self.moving = robot_obj.moving
        # self.currentlyTurning = robot_obj.currentlyTurning
        # #self.map = np.zeros( (10,10) )
        # self.canvas = robot_obj.canvas
        # self.view = robot_obj.view
        # self.cameraPositions= robot_obj.cameraPositions
        # self.sensorPositions=robot_obj.sensorPositions
        self.__dict__.update(robot_obj.__dict__)
        # # cf. Dudek and Jenkin, Computational Principles of Mobile Robotics
    def move(self,canvas,registryPassives,dt):
        if self.battery>0:
            self.battery -= 1
        if self.battery==0:
            self.vl = 0
            self.vr = 0
        for rr in registryPassives:
            if isinstance(rr,Charger) and self.distanceTo(rr)<80:
                self.battery += 10

        if self.vl==self.vr:
            R = 0
        else:
            R = (self.ll/2.0)*((self.vr+self.vl)/(self.vl-self.vr))
        omega = (self.vl-self.vr)/self.ll
        ICCx = self.x-R*math.sin(self.theta) #instantaneous centre of curvature
        ICCy = self.y+R*math.cos(self.theta)
        m = np.matrix( [ [math.cos(omega*dt), -math.sin(omega*dt), 0], \
                        [math.sin(omega*dt), math.cos(omega*dt), 0],  \
                        [0,0,1] ] )
        v1 = np.matrix([[self.x-ICCx],[self.y-ICCy],[self.theta]])
        v2 = np.matrix([[ICCx],[ICCy],[omega*dt]])
        newv = np.add(np.dot(m,v1),v2)
        newX = newv.item(0)
        newY = newv.item(1)
        newTheta = newv.item(2)
        newTheta = newTheta%(2.0*math.pi) #make sure angle doesn't go outside [0.0,2*pi)
        self.x = newX
        self.y = newY
        self.theta = newTheta
        if self.vl==self.vr: # straight line movement
            self.x += self.vr*math.cos(self.theta) #vr wlog
            self.y += self.vr*math.sin(self.theta)
        if self.x<0.0:
            self.x=999.0
        if self.x>1000.0:
            self.x = 0.0
        if self.y<0.0:
            self.y=999.0
        if self.y>1000.0:
            self.y = 0.0
        #self.updateMap()
        canvas.delete(self.name)
        self.draw(canvas)

    def look(self,registryActives):
        self.view = [0]*9
        for idx,pos in enumerate(self.cameraPositions):
            for cc in registryActives:
                if isinstance(cc,Cat):
                    dd = self.distanceTo(cc)
                    scaledDistance = max(400-dd,0)/400
                    ncx = cc.x-pos[0] #cat if robot were at 0,0
                    ncy = cc.y-pos[1]
                    #print(abs(angle-self.theta)%2.0*math.pi)
                    m = math.tan(self.theta)
                    A = m*m+1
                    B = 2*(-m*ncy-ncx)
                    r = 15 #radius
                    C = ncy*ncy - r*r + ncx*ncx
                    if B*B-4*A*C>=0 and scaledDistance>self.view[idx]:
                        self.view[idx] = scaledDistance
        self.canvas.delete("view")
        for vv in range(9):
            if self.view[vv]==0:
                self.canvas.create_rectangle(850+vv*15,50,850+vv*15+15,65,fill="white",tags="view")
            if self.view[vv]>0:
                colour = hex(15-math.floor(self.view[vv]*16.0)) #scale to 0-15 -> hex
                fillHex = "#"+colour[2]+colour[2]+colour[2]
                self.canvas.create_rectangle(850+vv*15,50,850+vv*15+15,65,fill=fillHex,tags="view")
        return self.view

    def pickUpAndPutDown(self,xp,yp):
        self.x = xp
        self.y = yp
        self.canvas.delete(self.name)
        self.draw(self.canvas)




    def senseCharger(self, registryPassives):
        lightL = 0.0
        lightR = 0.0
        for pp in registryPassives:
            if isinstance(pp,Charger):
                lx,ly = pp.getLocation()
                distanceL = math.sqrt( (lx-self.sensorPositions[0])*(lx-self.sensorPositions[0]) + \
                                       (ly-self.sensorPositions[1])*(ly-self.sensorPositions[1]) )
                distanceR = math.sqrt( (lx-self.sensorPositions[2])*(lx-self.sensorPositions[2]) + \
                                       (ly-self.sensorPositions[3])*(ly-self.sensorPositions[3]) )
                lightL += 200000/(distanceL*distanceL)
                lightR += 200000/(distanceR*distanceR)
        return lightL, lightR

    def senseHubs(self, registryPassives):
        signal = []
        for pp in registryPassives:
            if isinstance(pp,WiFiHub):
                lx,ly = pp.getLocation()
                distanceL = math.sqrt( (lx-self.sensorPositions[0])*(lx-self.sensorPositions[0]) + \
                                       (ly-self.sensorPositions[1])*(ly-self.sensorPositions[1]) )
                distanceR = math.sqrt( (lx-self.sensorPositions[2])*(lx-self.sensorPositions[2]) + \
                                       (ly-self.sensorPositions[3])*(ly-self.sensorPositions[3]) )
                signal.append(200000/(distanceL*distanceL))
                signal.append(200000/(distanceR*distanceR))
        return signal

    def distanceTo(self,obj):
        xx,yy = obj.getLocation()
        return math.sqrt( math.pow(self.x-xx,2) + math.pow(self.y-yy,2) )

    def collectDirt(self, canvas, registryPassives, count):
        toDelete = []
        for idx,rr in enumerate(registryPassives):
            if isinstance(rr,Dirt):
                if self.distanceTo(rr)<30:
                    canvas.delete(rr.name)
                    toDelete.append(idx)
                    count.itemCollected(canvas)
        for ii in sorted(toDelete,reverse=True):
            del registryPassives[ii]
        return registryPassives

    def transferFunction(self,chargerL,chargerR):
        # wandering behaviour
        if self.currentlyTurning==True:
            self.vl = -2.0
            self.vr = 2.0
            self.turning -= 1
        else:
            self.vl = 5.0
            self.vr = 5.0
            self.moving -= 1
        if self.moving==0 and not self.currentlyTurning:
            self.turning = random.randrange(20,40)
            self.currentlyTurning = True
        if self.turning==0 and self.currentlyTurning:
            self.moving = random.randrange(50,100)
            self.currentlyTurning = False
        #battery - these are later so they have priority
        if self.battery<600:
            if chargerR>chargerL:
                self.vl = 2.0
                self.vr = -2.0
            elif chargerR<chargerL:
                self.vl = -2.0
                self.vr = 2.0
            if abs(chargerR-chargerL)<chargerL*0.1: #approximately the same
                self.vl = 5.0
                self.vr = 5.0
            #self.vl = 5*math.sqrt(chargerR)
            #self.vr = 5*math.sqrt(chargerL)
        if chargerL+chargerR>200 and self.battery<1000:
            self.vl = 0.0
            self.vr = 0.0

    def collision(self,registryActives):
        collision = False
        for rr in registryActives:
            if isinstance(rr,Cat):
                if self.distanceTo(rr)<50.0:
                    playsound("385892__spacether__262312-steffcaffrey-cat-meow1.mp3",block=False)
                    collision = True
                    rr.jump()
        return collision


    def update_values(self,rr):
        rr.x = self.x
        rr.y = self.y
        rr.theta = self.theta
        #self.theta = 0
        rr.name = self.name
        rr.ll = self.ll #axle width
        rr.vl = self.vl
        rr.vr = self.vr
        rr.battery = self.battery
        rr.turning = self.turning
        rr.moving = self.moving
        rr.currentlyTurning = self.currentlyTurning
        #self.map = np.zeros( (10,10) )
        rr.canvas = self.canvas
        rr.view = self.view
        rr.cameraPositions= self.cameraPositions
        rr.sensorPositions=self.sensorPositions
        return rr
def example_use(rr):
    ddx=movingCat(rr)
    ddx.look(registryActives)
    chargerIntensityL, chargerIntensityR = ddx.senseCharger(registryPassives)
    ddx.transferFunction(chargerIntensityL, chargerIntensityR)

    rr.x = ddx.x
    rr.y = ddx.y
    rr.theta = ddx.theta
    #self.theta = 0
    rr.name = ddx.name
    rr.ll = ddx.ll #axle width
    rr.vl = ddx.vl
    rr.vr = ddx.vr
    rr.battery = ddx.battery
    rr.turning = ddx.turning
    rr.moving = ddx.moving
    rr.currentlyTurning = ddx.currentlyTurning
    #self.map = np.zeros( (10,10) )
    rr.canvas = ddx.canvas
    rr.view = ddx.view
    rr.cameraPositions= ddx.cameraPositions
    rr.sensorPositions=ddx.sensorPositions