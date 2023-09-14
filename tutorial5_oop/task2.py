'''
In this task, the student is expected to generate two new class

To recap, the objective is to create a robot that collect dust. and we want to know how much dirt has been collected
We can display this. Also we will create a dirt definition that will call the dirt class.
'''

class Counter:
    def __init__(self,canvas):
        self.dirtCollected = 0
        self.canvas = canvas
        self.canvas.create_text(70,50,text="Dirt collected: "+str(self.dirtCollected),tags="counter")

    def itemCollected(self, canvas):
        self.dirtCollected +=1
        self.canvas.itemconfigure("counter",text="Dirt collected: "+str(self.dirtCollected))


class Dirt:
    def __init__(self,namep,xx,yy):
        self.centreX = xx
        self.centreY = yy
        self.name = namep

    def draw(self,canvas):
        body = canvas.create_oval(self.centreX-1,self.centreY-1, \
                                  self.centreX+1,self.centreY+1, \
                                  fill="grey",tags=self.name)

    def getLocation(self):
        return self.centreX, self.centreY