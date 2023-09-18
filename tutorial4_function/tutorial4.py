'''

refactored the following code to have a keyword arguments,default value, arbitary keyword arguments and args kwargs

'''

import tkinter as tk

def make_print_status(status_text):
    print(f'Successfully create: {status_text}')

def check_condition_body_color(i, condition=True, colors=None):
    if colors is None:
        colors = {}

    if condition:
        body_color = colors.get(f"robot{i + 1}", {}).get("body_color", "gray")
    else:
        body_color = "gray"  # Default color if condition is False
    return body_color

def check_light_color(i, config, my_th, colors=None):
    if colors is None:
        colors = {}

    if config["center_x"] >= my_th:
        body_color_xx = "purple"
    else:
        body_color_xx = colors.get(f"robot{i + 1}", {}).get("light_color", "gray")
    return body_color_xx

def create_robot(i, canvas, config, condition=True, colors=None, my_th=500):
    constant_val = 0

    body_color = check_condition_body_color(i, condition, colors)
    body_color_xx = check_light_color(i, config, my_th, colors)

    canvas.create_polygon(config['robot_points'], fill=body_color, tags='robot')
    canvas.create_oval(config["center_x"], config["center_y"], config["center_x"], config["center_y"], fill=body_color_xx, tags='robot')

    canvas.create_oval(config["wheel1_x"] - constant_val, config["wheel1_y"] - constant_val, config["wheel1_x"] + constant_val, config["wheel1_y"] + constant_val, fill=colors.get(f"robot{i + 1}", {}).get("wheel_color_left", "gray"), tags='robot')
    canvas.create_oval(config["wheel2_x"] - constant_val, config["wheel2_y"] - constant_val, config["wheel2_x"] + constant_val, config["wheel2_y"] + constant_val, fill=colors.get(f"robot{i + 1}", {}).get("wheel_color_right", "gray"), tags='robot')
    canvas.create_oval(config["sensor1_x"] - constant_val, config["sensor1_y"] - constant_val, config["sensor1_x"] + constant_val, config["sensor1_y"] + constant_val, fill=colors.get(f"robot{i + 1}", {}).get("sensor_color", "gray"), tags='robot')
    canvas.create_oval(config["sensor2_x"] - constant_val, config["sensor2_y"] - constant_val, config["sensor2_x"] + constant_val, config["sensor2_y"] + constant_val, fill=colors.get(f"robot{i + 1}", {}).get("sensor_color", "gray"), tags='robot')

    text_x = config["center_x"] + 40
    text_y = config["center_y"]
    canvas.create_text(text_x, text_y, text=config["label"], anchor=tk.W)
    make_print_status(config["label"])

def main():
    root = tk.Tk()
    root.title("Customizable Robots")
    root.resizable(False, False)

    canvas = tk.Canvas(root, width=1000, height=1000)
    canvas.pack()

    import json
    with open('../robot_data.json', 'r') as json_file:
        data = json.load(json_file)

    # Access the data as needed
    colors = data["colors"]
    robot_configurations = data["robot_configurations"]

    condition = True
    constant_val = 0
    my_th = 500
    for i, config in enumerate(robot_configurations):
        create_robot(i, canvas, config, condition, colors, my_th)

    root.mainloop()

if __name__ == "__main__":
    main()
