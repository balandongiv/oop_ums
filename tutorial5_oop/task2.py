'''
In this task, the student is expected to generate two new class

To recap, the objective is to create a robot that collect dust. and we want to know how much dirt has been collected
We can display this. Also we will create a dirt definition that will call the dirt class.
'''
from robot_helper import initialise




'''

The first task it to create a new class called "Robot" that will be used to represent the robot in the simulation.

I will provide the following code to get you started:
Basiclly, you just need to copy paste the code from previous task and change the class name to Robot
'''
from passive_component import Dirt
import tkinter as tk
class Bot:

    def __init__(self,namep):


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

    def draw(self,i, canvas, config, condition=True, colors=None, my_th=500, **kwargs):
        '''
        In task 1, your task is to transfer the function create_robot to class method. I will provide the
        structure, but purposely leave some part for you to fill in.

        Instead of create_robot, we will use draw
        :param i:
        :param canvas:
        :param config:
        :param condition:
        :param colors:
        :param my_th:
        :param kwargs:
        :return:
        '''
        constant_val = 0

        body_color = self.check_condition_body_color(i, condition, colors)
        body_color_xx = self.check_light_color(i, config, my_th, colors)

        canvas.create_polygon(config['robot_points'], fill=body_color, tags='robot')
        canvas.create_oval(config["center_x"], config["center_y"], config["center_x"], config["center_y"], fill=body_color_xx, tags='robot')

        canvas.create_oval(config["wheel1_x"] - constant_val, config["wheel1_y"] - constant_val, config["wheel1_x"] + constant_val, config["wheel1_y"] + constant_val, fill=colors.get(f"robot{i + 1}", {}).get("wheel_color_left", "gray"), tags='robot')
        canvas.create_oval(config["wheel2_x"] - constant_val, config["wheel2_y"] - constant_val, config["wheel2_x"] + constant_val, config["wheel2_y"] + constant_val, fill=colors.get(f"robot{i + 1}", {}).get("wheel_color_right", "gray"), tags='robot')
        canvas.create_oval(config["sensor1_x"] - constant_val, config["sensor1_y"] - constant_val, config["sensor1_x"] + constant_val, config["sensor1_y"] + constant_val, fill=colors.get(f"robot{i + 1}", {}).get("sensor_color", "gray"), tags='robot')
        canvas.create_oval(config["sensor2_x"] - constant_val, config["sensor2_y"] - constant_val, config["sensor2_x"] + constant_val, config["sensor2_y"] + constant_val, fill=colors.get(f"robot{i + 1}", {}).get("sensor_color", "gray"), tags='robot')

        text_x = config["center_x"] + 40
        text_y = config["center_y"]
        canvas.create_text(text_x, text_y, text=config["label"], anchor=tk.W)
        # self.make_print_status(config["label"])


def register(canvas,robot_configurations,colors):



    condition = True
    constant_val = 0
    my_th = 500
    # Can suggest student to used zip and enumerate for this part
    for i, (config,clrx) in enumerate(zip(robot_configurations,colors)):
        robot_name='c'
        bot=Bot(robot_name)
        bot.draw(i, canvas, config, condition, colors, my_th)

    noOfDirt=30
    for i in range(0,noOfDirt):
        dirt = Dirt("Dirt"+str(i))
        # registryPassives.append(dirt)
        dirt.draw(canvas)

def main():
    import json
    with open('../robot_data.json', 'r') as json_file:
        data = json.load(json_file)

    # Access the data as needed
    colors = data["colors"]
    robot_configurations = data["robot_configurations"]

    window = tk.Tk()

    window = initialise(window)
    register(window,robot_configurations,colors)
    window.mainloop()

if __name__ == "__main__":
    main()
