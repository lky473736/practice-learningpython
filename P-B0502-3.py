'''# 터틀 그래픽에서 한 객체가 가지는 값 : 위치, 색깔, 길이값

import turtle
t = turtle.Turtle()

def passf() :
    pass # pass : 말 그대로 패스

lists = [[0, 0, "blue"], [-120, 0, "purple"], [60, 60, "red"],
         [-60, 60, "yellow"], [-180, 60, "green"]]

passf()

for x, y, z in lists :
    t.penup()
    t.goto(x, y)
    t.pendown() # 펜 움직이기 부분
    
    t.color(z, z) # 왜 여기서는 변수를 두 개로 잡는가? -> 처음 변수 : 선, 다음 변수 : 면
    t.begin_fill()
    t.circle(30)
    t.end_fill()
    
turtle.mainloop()'''

# turtle을 이용한 행위예술 ver 3

import random
import turtle

turtle.speed(0)

n = int(turtle.textinput("", "n?"))

for i in range (n) :
    turtle.forward(random.randint(0, 50))
    
    m = random.randint (1, 2)
    
    if m == 1 :
        turtle.left (random.randint(0, 360))
        
    else :
        turtle.right (random.randint(0, 360))
        
    turtle.write (m)

turtle.mainloop()