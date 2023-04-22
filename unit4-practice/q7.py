import turtle
import math

x = 0

t = turtle.Turtle()
t.shape("turtle")
t.color("red", "blue")

while True :
    t.goto(x, 200 * math.sin(x * 3.14/180))
    x += 1