import turtle

def Dessin():
    for steps in range(100):
        for c in ('blue', 'red', 'green'):
            turtle.color(c)
            turtle.forward(200)
            turtle.right(90)

Dessin()