'''import math

rad = float(input("반지름 입력 : "))

rst = 4 / 3 * math.pi * (rad ** 2)

print ("반지름 " + str(rad) + "의 구의 부피는 " + str(rst))

# stdin 오류 생길 때는 입력창에 exit() 쳐서 프로세스 초기화하기'''

# 올림픽 마크 그리기

import turtle
t = turtle.Turtle()
t.speed(10)
t.width(8)

t.pencolor("blue")
t.circle(100)
t.penup()
t.fd(150)
t.pendown()

t.pencolor("black")
t.circle(100)
t.penup()
t.fd(150)
t.pendown()

t.pencolor("red")
t.circle(100)
t.penup()

t.fd(-225)
t.rt(90)
t.fd(100)
t.rt(90)
t.rt(90)
t.rt(90)

t.pendown()
t.pencolor("yellow")
t.circle(100)
t.penup()
t.fd(150)
t.pendown()

t.pencolor("green")
t.circle(100)
t.penup()
t.fd(80)
t.pendown()

