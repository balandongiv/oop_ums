import tkinter as tk

# Create a tkinter window
root = tk.Tk()
root.title("Customizable Robot")

# Prevent the window from being resizable
root.resizable(False, False)

# Create a canvas widget within the window
canvas = tk.Canvas(root, width=1000, height=1000)
canvas.pack()

# Define colors for different parts of the robot
wheel_color_left = "red"
wheel_color_right = "green"
sensor_color = "gold"
light_color = "yellow"
body_color = "blue"

# Define points to create the robot's shape
robot_points = [
    293.9, 478.4,
    300.4, 538.1,
    360.1, 531.6,
    353.6, 471.9,
]

# Define positions for various robot components
center_x = 327
center_y = 505
wheel1_x = 330.3
wheel1_y = 534.8
wheel2_x = 323.7
wheel2_y = 475.2
sensor1_x = 354.6
sensor1_y = 481.8
sensor2_x = 359.0
sensor2_y = 521.6

# Create the robot on the canvas
canvas.create_polygon(robot_points, fill=body_color, tags='robot')
canvas.create_oval(center_x - 8, center_y - 8, center_x + 8, center_y + 8, fill=light_color, tags='robot')

# Constants for component size
constant_val = 3

# Create robot components on the canvas
canvas.create_oval(wheel1_x - constant_val, wheel1_y - constant_val, wheel1_x + constant_val, wheel1_y + constant_val, fill=wheel_color_left, tags='robot')
canvas.create_oval(wheel2_x - constant_val, wheel2_y - constant_val, wheel2_x + constant_val, wheel2_y + constant_val, fill=wheel_color_right, tags='robot')
canvas.create_oval(sensor1_x - constant_val, sensor1_y - constant_val, sensor1_x + constant_val, sensor1_y + constant_val, fill=sensor_color, tags='robot')
canvas.create_oval(sensor2_x - constant_val, sensor2_y - constant_val, sensor2_x + constant_val, sensor2_y + constant_val, fill=sensor_color, tags='robot')

# Add text next to the robot
text_x = center_x + 40  # Adjust the X-coordinate to position the text
text_y = center_y
canvas.create_text(text_x, text_y, text="Robot One", anchor=tk.W)

# Main tkinter event loop
root.mainloop()
