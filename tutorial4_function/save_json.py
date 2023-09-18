import json

# Your data
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

# Save the data as a JSON file
with open('../robot_data.json', 'w') as json_file:
    json.dump({"colors": colors, "robot_configurations": robot_configurations}, json_file)
