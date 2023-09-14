'''

In this task, we will add a definition to create dust on the canvas. The dust will be created randomly on the canvas.

'''



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