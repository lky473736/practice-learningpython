import turtle

n = int(turtle.textinput("", "n?"))

if n == 0 :
    rad = int(turtle.textinput("", "rad?"))
    turtle.circle(rad)
    
else :
    len = int(turtle.textinput("", "len?"))
    for i in range (n) :
        turtle.forward(len)
        turtle.left(360/n)
        
turtle.mainloop()