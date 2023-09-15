'''

For week 7, you will be creating a program that will be able to read a file and do some plotting

In this file, I already remove the config file.

still not working!!


'''
import random
import math
import tkinter as tk
import numpy as np
np.random.seed(12345)

class Counter:
    def __init__(self,canvas):
        self.dirtCollected = 0
        self.canvas = canvas
        self.canvas.create_text(70,50,text="Dirt collected: "+str(self.dirtCollected),tags="counter")

    def itemCollected(self, canvas):
        self.dirtCollected +=1
        self.canvas.itemconfigure("counter",text="Dirt collected: "+str(self.dirtCollected))

class Dirt:
    def __init__(self,namep):
        self.centreX = np.random.randint(100, 900)
        self.centreY = np.random.randint(100, 900)

        self.name = namep

    def draw(self,canvas):
        dirt_constant=4
        body = canvas.create_oval(self.centreX-dirt_constant,self.centreY-dirt_constant, \
                                  self.centreX+dirt_constant,self.centreY+dirt_constant, \
                                  fill="grey",tags=self.name)

    def getLocation(self):
        return self.centreX, self.centreY

'''

The first task it to create a new class called "Robot" that will be used to represent the robot in the simulation.

I will provide the following code to get you started:
Basiclly, you just need to copy paste the code from previous task and change the class name to Robot
'''

class Bot:

    def __init__(self,namep,canvasp):
        self.x = np.random.randint(100, 900)
        self.y = np.random.randint(100, 900)
        self.theta = np.random.uniform(0.0, 2.0 * math.pi)
        #self.theta = 0
        self.name = namep
        self.ll = 60 #axle width
        self.vl = 0.0
        self.vr = 0.0
        self.battery = 1000
        self.turning = 0
        self.moving = np.random.randint(50, 101)
        self.currentlyTurning = False
        self.canvas = canvasp


    def make_print_status(status_text):
        '''
        In the first task, I will give an example of how to use the class method. And how you
        can transfer the function to class method under the class Robot.
        Specifically, I will transfer the function make_print_status to class method.
        :return:
        '''
        print(f'Successfully create: {status_text}')

    def check_condition_body_color(self,i, condition=True, colors=None):
        '''
        In the first task, I will give an example of how to use the class method. And how you
        can transfer the function to class method under the class Robot.
        Specifically, I will transfer the function check_condition_body_color.
        :return:
        '''
        if colors is None:
            colors = {}

        if condition:
            body_color = colors.get(f"robot{i + 1}", {}).get("body_color", "gray")
        else:
            body_color = "gray"  # Default color if condition is False
        return body_color

    def check_light_color(self,i, config, my_th, colors=None):
        '''
        In the first task, I will give an example of how to use the class method. And how you
        can transfer the function to class method under the class Robot.
        Specifically, I will transfer the function check_light_color to class method.
        :return:
        '''

        if colors is None:
            colors = {}

        if config["center_x"] >= my_th:
            body_color_xx = "purple"
        else:
            body_color_xx = colors.get(f"robot{i + 1}", {}).get("light_color", "gray")
        return body_color_xx

    def draw(self,canvas):


        angle = np.pi / 2.0
        points = [
            (self.x + 30 * np.sin(self.theta)) - 30 * np.sin((angle) - self.theta),
            (self.y - 30 * np.cos(self.theta)) - 30 * np.cos((angle) - self.theta),
            (self.x - 30 * np.sin(self.theta)) - 30 * np.sin((angle) - self.theta),
            (self.y + 30 * np.cos(self.theta)) - 30 * np.cos((angle) - self.theta),
            (self.x - 30 * np.sin(self.theta)) + 30 * np.sin((angle) - self.theta),
            (self.y + 30 * np.cos(self.theta)) + 30 * np.cos((angle) - self.theta),
            (self.x + 30 * np.sin(self.theta)) + 30 * np.sin((angle) - self.theta),
            (self.y - 30 * np.cos(self.theta)) + 30 * np.cos((angle) - self.theta),
            ]
        canvas.create_polygon(points, fill="blue", tags=self.name)

        self.sensorPositions = [
            (self.x + 20 * np.sin(self.theta)) + 30 * np.sin((math.pi / 2.0) - self.theta),
            (self.y - 20 * np.cos(self.theta)) + 30 * np.cos((math.pi / 2.0) - self.theta),
            (self.x - 20 * np.sin(self.theta)) + 30 * np.sin((math.pi / 2.0) - self.theta),
            (self.y + 20 * np.cos(self.theta)) + 30 * np.cos((math.pi / 2.0) - self.theta),
            ]

        centre1PosX = self.x
        centre1PosY = self.y
        canvas.create_oval(centre1PosX-15,centre1PosY-15, \
                           centre1PosX+15,centre1PosY+15, \
                           fill="gold",tags=self.name)

        # Generate the battery text
        canvas.create_text(self.x,self.y,text=str(self.battery),tags=self.name)

        wheel1PosX = self.x - 30*math.sin(self.theta)
        wheel1PosY = self.y + 30*math.cos(self.theta)
        canvas.create_oval(wheel1PosX-3,wheel1PosY-3, \
                           wheel1PosX+3,wheel1PosY+3, \
                           fill="red",tags=self.name)

        wheel2PosX = self.x + 30*math.sin(self.theta)
        wheel2PosY = self.y - 30*math.cos(self.theta)
        canvas.create_oval(wheel2PosX-3,wheel2PosY-3, \
                           wheel2PosX+3,wheel2PosY+3, \
                           fill="green",tags=self.name)

        sensor1PosX = self.sensorPositions[0]
        sensor1PosY = self.sensorPositions[1]
        sensor2PosX = self.sensorPositions[2]
        sensor2PosY = self.sensorPositions[3]
        canvas.create_oval(sensor1PosX-3,sensor1PosY-3, \
                           sensor1PosX+3,sensor1PosY+3, \
                           fill="yellow",tags=self.name)
        canvas.create_oval(sensor2PosX-3,sensor2PosY-3, \
                           sensor2PosX+3,sensor2PosY+3, \
                           fill="yellow",tags=self.name)
        # Maybe in tutorial 2 or 3, we can add logic, say, if number of robot greater than two, then, no need to print the label
        # text_x = config["center_x"] + 40
        # text_y = config["center_y"]
        # canvas.create_text(text_x, text_y, text=config["label"], anchor=tk.W)

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

class try_move:
    def __init__(self,robot_obj):
        hhh=22
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
        c=1


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
def initialise(window):
    window.resizable(False,False)
    canvas = tk.Canvas(window,width=1000,height=1000)
    canvas.pack()
    return canvas

def buttonClicked(x,y,registryActives):
    for rr in registryActives:
        if isinstance(rr,Bot):
            rr.x = x
            rr.y = y
def register(canvas):
    registryActives = []
    registryPassives = []
    noOfBots = 30
    noOfDirt = 300
    for i in range(0,noOfBots):
        bot = Bot("Bot"+str(i),canvas)
        registryActives.append(bot)
        bot.draw(canvas)
    charger = Charger("Charger")
    registryPassives.append(charger)
    charger.draw(canvas)
    hub1 = WiFiHub("Hub1",950,50)
    registryPassives.append(hub1)
    hub1.draw(canvas)
    hub2 = WiFiHub("Hub1",50,500)
    registryPassives.append(hub2)
    hub2.draw(canvas)
    for i in range(0,noOfDirt):
        dirt = Dirt("Dirt"+str(i))
        registryPassives.append(dirt)
        dirt.draw(canvas)
    count = Counter(canvas)
    canvas.bind( "<Button-1>", lambda event: buttonClicked(event.x,event.y,registryActives) )
    return registryActives, registryPassives, count
def moveIt(canvas,registryActives,registryPassives,count,moves):
    moves += 1
    for rr in registryActives:
        tmx=try_move(rr)
        chargerIntensityL, chargerIntensityR = tmx.senseCharger(registryPassives)
        tmx.transferFunction(chargerIntensityL, chargerIntensityR)
        tmx.move(canvas,registryPassives,1.0)
        ## update back the value
        rr.battery= tmx.battery
        rr.canvas= tmx.canvas
        rr.currentlyTurning= tmx.currentlyTurning
        rr.ll= tmx.ll
        rr.moving= tmx.moving
        rr.name= tmx.name
        rr.sensorPositions= tmx.sensorPositions
        rr.theta= tmx.theta
        rr.turning= tmx.turning
        rr.vl= tmx.vl
        rr.vr= tmx.vr
        rr.x= tmx.x
        rr.y= tmx.y

        registryPassives = tmx.collectDirt(canvas,registryPassives, count)
        numberOfMoves = 5000
        print(f'The number of moves is {moves}')
        if moves>numberOfMoves:
            print("total dirt collected in",numberOfMoves,"moves is",count.dirtCollected)
            sys.exit()
    canvas.after(20,moveIt,canvas,registryActives,registryPassives,count,moves)
def main():


    window = tk.Tk()

    window = initialise(window)
    registryActives, registryPassives, count =register(window)
    moves = 0
    moveIt(window,registryActives,registryPassives, count, moves)

    window.mainloop()

    ### I need some return value here, so that I can use it in the next function


if __name__ == "__main__":
    main()
