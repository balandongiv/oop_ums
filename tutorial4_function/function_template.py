import tkinter as tk

def make_print_status( status_text):
    print(f'Succesfully create: {status_text}')
def create_robot(i,canvas, config, condition, colors,my_th):
    constant_val = 0

    # Check the condition and change the body color accordingly
    if condition:
        body_color = colors[f"robot{i + 1}"]["body_color"]
    else:
        body_color = "gray"  # Default color if condition is False

    # Check if the robot's center x-coordinate is greater than or equal to 500
    if config["center_x"] >= my_th:
        body_color_xx = "purple"
    else:
        body_color_xx =colors[f"robot{i + 1}"]["light_color"]

    # Create the robot on the canvas
    canvas.create_polygon(config['robot_points'], fill=body_color, tags='robot')

    # Antena
    # canvas.create_oval(config["center_x"] - 8, config["center_y"] - 8, config["center_x"] + 8, config["center_y"] + 8, fill=colors[f"robot{i + 1}"]["light_color"], tags='robot')
    canvas.create_oval(config["center_x"] - 0, config["center_y"] - 0, config["center_x"] + 0, config["center_y"] + 0, fill=body_color_xx , tags='robot')

    # Create robot components on the canvas
    canvas.create_oval(config["wheel1_x"] - constant_val, config["wheel1_y"] - constant_val, config["wheel1_x"] + constant_val, config["wheel1_y"] + constant_val, fill=colors[f"robot{i + 1}"]["wheel_color_left"], tags='robot')
    canvas.create_oval(config["wheel2_x"] - constant_val, config["wheel2_y"] - constant_val, config["wheel2_x"] + constant_val, config["wheel2_y"] + constant_val, fill=colors[f"robot{i + 1}"]["wheel_color_right"], tags='robot')
    canvas.create_oval(config["sensor1_x"] - constant_val, config["sensor1_y"] - constant_val, config["sensor1_x"] + constant_val, config["sensor1_y"] + constant_val, fill=colors[f"robot{i + 1}"]["sensor_color"], tags='robot')
    canvas.create_oval(config["sensor2_x"] - constant_val, config["sensor2_y"] - constant_val, config["sensor2_x"] + constant_val, config["sensor2_y"] + constant_val, fill=colors[f"robot{i + 1}"]["sensor_color"], tags='robot')

    # Add text next to the robot
    text_x = config["center_x"] + 40  # Adjust the X-coordinate to position the text
    text_y = config["center_y"]
    canvas.create_text(text_x, text_y, text=config["label"], anchor=tk.W)
    make_print_status(config["label"])

def main():
    root = tk.Tk()
    root.title("Customizable Robots")
    root.resizable(False, False)

    canvas = tk.Canvas(root, width=1000, height=1000)
    canvas.pack()

    colors = {
        "robot1": {
            "wheel_color_left": "red",
            "wheel_color_right": "green",
            "sensor_color": "gold",
            "light_color": "yellow",
            "body_color": "blue",
        },
        "robot2": {
            "wheel_color_left": "orange",
            "wheel_color_right": "purple",
            "sensor_color": "silver",
            "light_color": "pink",
            "body_color": "cyan",
        },
    }

    robot_configurations = [
        {
            "center_x": 327,
            "center_y": 505,
            "wheel1_x": 330.3,
            "wheel1_y": 534.8,
            "wheel2_x": 323.7,
            "wheel2_y": 475.2,
            "sensor1_x": 354.6,
            "sensor1_y": 481.8,
            "sensor2_x": 359.0,
            "sensor2_y": 521.6,
            "label": "Robot One",
            'robot_points': [
                293.9, 478.4,
                300.4, 538.1,
                360.1, 531.6,
                353.6, 471.9,
            ]
        },
        {
            "center_x": 627,
            "center_y": 505,
            "wheel1_x": 630.3,
            "wheel1_y": 534.8,
            "wheel2_x": 623.7,
            "wheel2_y": 475.2,
            "sensor1_x": 654.6,
            "sensor1_y": 481.8,
            "sensor2_x": 659.0,
            "sensor2_y": 521.6,
            "label": "Robot Two",
            'robot_points': [
                593.9, 478.4,
                600.4, 538.1,
                660.1, 531.6,
                653.6, 471.9,
            ]
        },
    ]
    condition = True
    constant_val = 0
    my_th=500
    for i, config in enumerate(robot_configurations):
        create_robot(i,canvas, config, condition, colors,my_th)

    root.mainloop()

if __name__ == "__main__":
    main()
