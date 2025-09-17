import turtle

turtle.speed(2)
segment = 100

def draw_polygon(cote):
    for i in range(cote):
        turtle.forward(segment)
        turtle.left(360 / cote)

    # if cote == 3:
    #     for i in range(cote):
    #         turtle.forward(segment)
    #         turtle.left(120)
    # if cote == 4:
    #     for i in range(cote):
    #         turtle.forward(segment)
    #         turtle.left(90)
    # if cote == 5:
    #     for i in range(cote):
    #         turtle.forward(segment)
    #         turtle.left(72)
    # if cote == 6:
    #     for i in range(cote):
    #         turtle.forward(segment)
    #         turtle.left(60)
        
draw_polygon(10)