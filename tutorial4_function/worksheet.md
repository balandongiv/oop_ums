For this tutorial.
the objective is to convert some of the code from the previous tutorial into functions.

First download the file `function_template.py` from itel.
Take a moment to read the code and understand what it does.
If you notice, the code is the same as the code from the previous tutorial.However, the code is now in a function.

There are several functions in the code.
- make_print_status
- create_robot
- main

Apart from that, we also being introduce with a new statement

```python
if __name__ == "__main__":
    main()
```

This statement is used to call the main function.

Lets understand the flow of the function calling.
When we run the code, the first function that will be called is the main function. Under the main function, we can call other function.
Specifically,in this case, we are calling the function `create_robot` under the for loop.
With each loop, the function `create_robot` will be called with different parameters.

Under the `create_robot` function, we can see that there are logic condition (i.e., if-else statemetn). Apart from that
there are code for creating the canvas object.

At the end of the `create_robot` function, we are calling another function, `make_print_status`.

What is the take home message, basicly, we can create a function and call it from another function.

# Task 1
If you notice, the configuration file is store in a python file. However, it is not a good practice to store the configuration file in a python file.
Instead, we can store the configuration file in a json file.

For this task, we will create a function for reading the configuration file.
For more detail on how to read a json file, you can refer to the following link:
also, more detail on how to create json file can be found here:

Lets do some clean up first.
- remove the configuration file from the python file

means, remove the following code undere the main function from the python file:

```python
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
```
Then, add the following line of code under the main function. add the line just after the `canvas.pack()` line:

```python
    import json
    with open('../robot_data.json', 'r') as json_file:
        data = json.load(json_file)

    # Access the data as needed
    colors = data["colors"]
    robot_configurations = data["robot_configurations"]
```
To ensure that the code is working, you can run the code and make sure that the code does not produce any error. if there is gui appear, mean the code is working fine

# Task 2

Now that you aware where you can read a function from another function, lets create more function by extracting out
some of the logic from the function `create_robot`

## Task 2a
Lets create a function for checking a condition of body color.

Lets have the function header as follow:

```python
def check_condition_body_color(condition,colors,i):
    '''
    Add more function here
    '''
    return body_color
```
To call the function in the function `create_robot`, you can call the function
`check_condition_body_color` as follow:

```python
    body_color = check_condition_body_color(condition,colors,i)
```

## Task 2b

Similarly, lets create a function for checking a condition of light  color.
Lets have the function header as follow:
    
```python
def check_light_color(config,colors,i,my_th):
    '''
    Add more function here
    '''
    return body_color_xx

```
To call the function in the function `create_robot`, you can call the function
`check_light_color` as follow:
```python
    body_color_xx = check_light_color(config,colors,i,my_th)
```


# Task 4
At this stage, you should be familiar with positional argument.
lets use keyword argument for the function `create_robot`

more thing to do: in the python file, this tutorial was known as `tutorial4.py`

## Task 4a

For the `create_robot` function, lets use keyword argument for the function.

The function header should be as follow:

```python
def create_robot(i, canvas, config, condition=True, colors=None, my_th=500):
    '''
    The other code is similar
    '''
```

## Task 4b

For the `check_condition_body_color` function, lets use keyword argument for the function.
The function header should be as follow:

```python
def check_condition_body_color(i, condition=True, colors=None):
    '''
    Add more function here
    '''
    return body_color
```
In this case,we just assume, no colors is being passed to the function.

## Task 4c

For the `check_condition_body_color` function, lets use keyword argument for the function.
The function header should be as follow:

```python
def check_condition_body_color(i, condition=True, colors=None):
    '''
    Add more function here
    '''

``` 

# Task 5
In the draft, it seems I want to ask the student to create the following

```python
def placeDirt(registryPassives,canvas):
    #places dirt in a specific configuration
    map = np.zeros( (10,10), dtype=np.int16)
    for xx in range(10):
        for yy in range(10):
            map[xx][yy] = random.randrange(1,3)
    for yy in range(0,10):
        map[8][yy] = 10
    for xx in range(1,8):
        map[xx][0] = 10
    map[0][0] = 1
    map[9][9] = 0
    i = 0
    for xx in range(10):
        for yy in range(10):
            for _ in range(map[xx][yy]):
                dirtX = xx*100 + random.randrange(0,99)
                dirtY = yy*100 + random.randrange(0,99)
                dirt = Dirt("Dirt"+str(i),dirtX,dirtY)
                registryPassives.append(dirt)
                dirt.draw(canvas)
                i += 1
    # print(np.transpose(map))
    return map
```




## Count as assignment
I will use this as a bonus task, and this will count as mark

Create a function called `initialise` that take the `window` as an argument.
Then, the function should handle the following:
- resize the window as `false` for both x and y axis
- create a canvas object with the size of 1000x1000
- pack the canvas object
- return the canvas object

** Note** : The syntax for the four points above is actually available in the `main` function.Please make sure to delete the respective code from the `main` function after you have created the `initialise` function.

to call the function, you can call the function as follow:

```python
        window = tk.Tk()
        window = initialise(window)
```

this is a bonus task, and this will count as mark

Similarly

print the `colors` and `robot_configurations` variable.
several function being called.

assume now, we start with this functin, which is originally from the previous tutorial:

# First task: create a function for creating a robot

Lets create a function with the name 'main'. which is as follow

```python
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
    my_th=500
    #for i, config in enumerate(robot_configurations):
    #    create_robot(i,canvas, config, condition, colors,my_th)

    root.mainloop()
```
Under the main, we can store the code which
For convenience sake, we will use the same code as the previous tutorial.However, for starting, the configuration file
will be store in a json file instead of a python file.

For convenience, I already store the configuration file in a json file.
you can download and access it by using the following code:

```python
    import json

with open('../robot_data.json', 'r') as json_file:
    data = json.load(json_file)
```
If you print the json file, you will see that it is a dictionary with the following structure:

```python
{'robot': {'name': 'robot1', 'type': 'robot', 'position': [0, 0, 0], 'orientation': [0, 0, 0]},
 'objects': [{'name': 'object1', 'type': 'object', 'position': [0, 0, 0], 'orientation': [0, 0, 0]},
             {'name': 'object2', 'type': 'object', 'position': [0, 0, 0], 'orientation': [0, 0, 0]}],
 'walls': [{'name': 'wall1', 'type': 'wall', 'position': [0, 0, 0], 'orientation': [0, 0, 0]},
           {'name': 'wall2', 'type': 'wall', 'position': [0, 0, 0], 'orientation': [0, 0, 0]}]}
```
which is the same as the python file from the previous tutorial.


`