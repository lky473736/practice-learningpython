# 4) 클릭하면 정사각형 생기기

import turtle
import random

colorlist = ['red', 'blue', 'green', 'yellow', 'pink', 'black']

def clicker (x, y) :
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    square()
    
def square() :
    turtle.begin_fill()
    turtle.color(random.choice(colorlist))
    
    for i in range (4) :
        turtle.forward (100)
        turtle.right (90)
        
    turtle.end_fill()
    
turtle.onscreenclick (clicker)
turtle.mainloop()