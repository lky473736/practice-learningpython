import turtle
import random

one = turtle.Turtle()
one.color ("blue")
one.shape ("arrow")

two = turtle.Turtle()
two.color ("red")
two.shape ("turtle")

dice = [1, 2, 3, 4, 5, 6]

one_distance = random.choice(dice)
two_distance = random.choice(dice)

two.penup()
two.goto (0, -100)
two.pendown()

one.fd (one_distance * 40)
one.circle (30)

two.fd (two_distance * 40)
two.circle (30)

turtle.mainloop()