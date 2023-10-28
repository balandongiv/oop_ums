import tkinter as tk

# change here
def initialise(window):
    window.resizable(False,False)
    canvas = tk.Canvas(window,width=1000,height=1000)
    canvas.pack()
    return canvas

def buttonClicked(x,y,registryActives,Bot):
    '''
    Bot is a class
    :param x:
    :param y:
    :param registryActives:
    :param Bot:
    :return:
    '''
    for rr in registryActives:
        if isinstance(rr,Bot):
            rr.x = x
            rr.y = y