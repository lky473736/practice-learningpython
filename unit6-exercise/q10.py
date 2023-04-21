import turtle
import random

t = turtle.Turtle()
t.shape('turtle')

t.speed(0)

r = random.Random()

colorlist = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', 'gray']

number = int(turtle.textinput("", "number?"))

for i in range (number) : 
    random_k = r.randint(0, len(colorlist) - 1)
    random_x = r.randint(-300, 300)
    random_y = r.randint(-300, 300)
    
    t.begin_fill()
    t.fillcolor(colorlist[random_k])
    
    for j in range (4) :
        t.fd(80)
        t.lt(90)
        
    t.end_fill()
        
    t.penup()
    t.goto(random_x, random_y)
    t.pendown()
    
turtle.mainloop()