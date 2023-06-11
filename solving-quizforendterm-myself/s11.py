import turtle
import random

def clicker(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    tri()

def tri():
    turtle.begin_fill()
    
    for i in range(3):
        turtle.forward(100)
        turtle.left(120)

    turtle.end_fill()

turtle.onscreenclick(clicker)
turtle.mainloop()
