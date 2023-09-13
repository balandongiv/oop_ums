import tkinter as tk
# Generate two robot using for loops


# Create a tkinter window
root = tk.Tk()
root.title("Customizable Robots")

# Prevent the window from being resizable
root.resizable(False, False)

# Create a canvas widget within the window
canvas = tk.Canvas(root, width=1000, height=1000)
canvas.pack()

# Define colors for different parts of the robots
colors = {
    "wheel_color_left": "red",
    "wheel_color_right": "green",
    "sensor_color": "gold",
    "light_color": "yellow",
    "body_color": "blue",
}

# Define a list of robot configurations
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
        'robot_points' : [
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
        'robot_points' : [
            593.9, 478.4,
            600.4, 538.1,
            660.1, 531.6,
            653.6, 471.9,
        ]
    },
]

# Create robots using a loop
constant_val = 3
for config in robot_configurations:
    # Create the robot on the canvas
    canvas.create_polygon(config['robot_points'], fill=colors["body_color"], tags='robot')
    canvas.create_oval(config["center_x"] - 8, config["center_y"] - 8, config["center_x"] + 8, config["center_y"] + 8, fill=colors["light_color"], tags='robot')

    # Create robot components on the canvas
    canvas.create_oval(config["wheel1_x"] - constant_val, config["wheel1_y"] - constant_val, config["wheel1_x"] + constant_val, config["wheel1_y"] + constant_val, fill=colors["wheel_color_left"], tags='robot')
    canvas.create_oval(config["wheel2_x"] - constant_val, config["wheel2_y"] - constant_val, config["wheel2_x"] + constant_val, config["wheel2_y"] + constant_val, fill=colors["wheel_color_right"], tags='robot')
    canvas.create_oval(config["sensor1_x"] - constant_val, config["sensor1_y"] - constant_val, config["sensor1_x"] + constant_val, config["sensor1_y"] + constant_val, fill=colors["sensor_color"], tags='robot')
    canvas.create_oval(config["sensor2_x"] - constant_val, config["sensor2_y"] - constant_val, config["sensor2_x"] + constant_val, config["sensor2_y"] + constant_val, fill=colors["sensor_color"], tags='robot')

    # Add text next to the robot
    text_x = config["center_x"] + 40  # Adjust the X-coordinate to position the text
    text_y = config["center_y"]
    canvas.create_text(text_x, text_y, text=config["label"], anchor=tk.W)

# Main tkinter event loop
root.mainloop()
