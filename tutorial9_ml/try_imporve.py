import math

from dynamic_component import Cat


class movingCat:
    def __init__(self,robot_obj):
        self.x = robot_obj.x
        self.y = robot_obj.y
        self.theta = robot_obj.theta
        #self.theta = 0
        self.name = robot_obj.name
        self.ll = robot_obj.ll #axle width
        self.vl = robot_obj.vl
        self.vr = robot_obj.vr
        self.battery = robot_obj.battery
        self.turning = robot_obj.turning
        self.moving = robot_obj.moving
        self.currentlyTurning = robot_obj.currentlyTurning
        #self.map = np.zeros( (10,10) )
        self.canvas = robot_obj.canvas
        self.view = robot_obj.view
        self.cameraPositions= robot_obj.cameraPositions
        self.sensorPositions=robot_obj.sensorPositions
        # # cf. Dudek and Jenkin, Computational Principles of Mobile Robotics


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


        return collision

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