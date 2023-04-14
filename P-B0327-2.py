'''
import turtle 

def triangle():
    for i in range(3) :
        t.fd (leng)
        t.right(120)

def square():
    for i in range(4) : # 4번 반복한다
        t.fd (leng) # fd : forward (앞으로 간다)
        t.right (90) # 오른쪽으로 90도 꺾는다
    


t = turtle.Turtle()
t.shape ("turtle") # turtle, arrow, circle ... 다양한 커서 모양을 가질 수 있다
leng = int(input("길이 : ")) # 길이를 입력받는다
print ("삼각형 : 1, 사각형 : 2, 원 : 3")
choice = int(input("당신의 선택 : "))

if choice == 1 : # 정삼각형
    triangle()
    
elif choice == 2 : # 정사각형
    square()
    
elif choice == 3 : # 원
    t.circle(leng+30)
    
"""
t.penup() # 펜을 든다. 궤적이 그려지지 않는다
t.fd (leng+50)
t.pendown() # 다시 펜을 내린다. 이때부터는 궤적이 그려진다.
"""

turtle.mainloop()
'''

# 시에르핀스키 삼각형
# 시에르핀스키 삼각형 : 프랙탈 이론을 적용한 n-tuple의 개변태 삼각형

# length : 길이
# depth : n (tuple number)

# 재귀변수 사용

# gpt-3의 도움을 받음

import turtle

def draw_fractal_triangle(length, depth):
    if depth == 0:
        for i in range(3):
            turtle.forward(length)
            turtle.left(120)
    else:
        draw_fractal_triangle(length/2, depth-1)
        turtle.forward(length/2)
        draw_fractal_triangle(length/2, depth-1)
        turtle.backward(length/2)
        turtle.left(60)
        turtle.forward(length/2)
        turtle.right(60)
        draw_fractal_triangle(length/2, depth-1)
        turtle.left(60)
        turtle.backward(length/2)
        turtle.right(60)

# set up turtle
turtle.speed('fastest')
turtle.penup()
turtle.goto(-200, 0)
turtle.pendown()

# draw fractal triangle
length = int(turtle.textinput("", "length"))
depth = int(turtle.textinput("", "depth"))
draw_fractal_triangle(length, depth)

# hide turtle
turtle.hideturtle()

# keep window open until it's manually closed
turtle.done()
