import math
import random

import numpy as np

from passive_component import Dirt, WiFiHub, Charger


class try_move:
    def __init__(self,robot_obj):
        self.currentlyTurning=robot_obj.currentlyTurning
        self.ll=robot_obj.ll
        self.moving=robot_obj.moving
        self.name=robot_obj.name
        self.sensorPositions=robot_obj.sensorPositions
        self.theta=robot_obj.theta
        self.turning=robot_obj.turning
        self.vl=robot_obj.vl
        self.vr=robot_obj.vr
        self.x=robot_obj.x
        self.y=robot_obj.y
        self.battery=robot_obj.battery
        self.draw=robot_obj.draw
        self.canvas = robot_obj.canvas
    # cf. Dudek and Jenkin, Computational Principles of Mobile Robotics
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
                         [math.sin(omega*dt), math.cos(omega*dt), 0], \
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
            # if chargerR>chargerL:
            #     self.vl = 2.0
            #     self.vr = -2.0
            # elif chargerR<chargerL:
            #     self.vl = -2.0
            #     self.vr = 2.0
            # if abs(chargerR-chargerL)<chargerL*0.1: #approximately the same
            #     self.vl = 5.0
            #     self.vr = 5.0
            self.vl = 5*math.sqrt(chargerR)
            self.vr = 5*math.sqrt(chargerL)
        if chargerL+chargerR>200 and self.battery<1000:
            self.vl = 0.0
            self.vr = 0.0