import turtle

def clicker (x, y) :
       turtle.penup()
       turtle.goto(x,y)
       turtle.pendown()
       square()

def square() :
       turtle.begin_fill()
       turtle.color('red')
       
       for i in range (4) :
             turtle.fd (100)
             turtle.lt (90)
       
       turtle.end_fill()

turtle.onscreenclick(clicker)
turtle.mainloop()