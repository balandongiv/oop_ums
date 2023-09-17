'''
In this file, I already remove the config file.




'''
import random
import math
import tkinter as tk
import numpy as np
np.random.seed(12345)



from passive_component import Dirt,Counter
from robot_helper import initialise
'''

The first task it to create a new class called "Robot" that will be used to represent the robot in the simulation.

I will provide the following code to get you started:
Basiclly, you just need to copy paste the code from previous task and change the class name to Robot
'''

class Bot:

    def __init__(self,namep):
        self.x = np.random.randint(100, 900)
        self.y = np.random.randint(100, 900)
        # self.theta = np.random.uniform(0.0, 2.0 * math.pi)
        self.theta = 0
        self.name = namep



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
        # batteryText = canvas.create_text(self.x,self.y,text=str(self.battery),tags=self.name)

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



def register(canvas):

    # add the two liness

    condition = True
    constant_val = 0
    my_th = 500
    # Can suggest student to used zip and enumerate for this part
    noOfBots=5
    for i in range(0,noOfBots):
        bot = Bot("Bot"+str(i))
        # registryActives.append(bot)
        bot.draw(canvas)

    noOfDirt=30
    for i in range(0,noOfDirt):
        dirt = Dirt("Dirt"+str(i))
        # registryPassives.append(dirt)
        dirt.draw(canvas)
    count = Counter(canvas)

def main():


    window = tk.Tk()

    window = initialise(window)
    register(window)
    window.mainloop()

if __name__ == "__main__":
    main()
