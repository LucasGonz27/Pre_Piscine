import turtle

turtle.speed(2)

def spiral():
    for i in range(100):
        turtle.color('red')
        turtle.forward(i)
        turtle.right(30)
spiral()