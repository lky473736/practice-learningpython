'''
import turtle
t = turtle.Turtle()
t.shape ("turtle")

#rad = int (input ("입력 : "))
#저 위엔 '일반입력문구'임. 인터프리터에서 입력 받음

rad = turtle.textinput ("", "입력 : ")
#turtle 창에서 입력을 받게끔 하는 코드임
# = 그래픽 입력
len = turtle.textinput ("", "입력 : ")

rad = int(rad)
#rad를 정수형으로 바꾼다 (입력은 문자형이니깐)
len = int(len)

for i in range(3) :
    t.circle(rad) # 반지름이 100인 원 그림
    t.fd (len) # 100 나아감 

# for i in range (n)
# : 들여쓰기 한 부분이 n번 반복된다.


turtle.mainloop()
turtle.bye()
turtle.exitonclick() 

# exitonclick : 누를 때 나가짐 
'''

# 밑변과 높이를 이용하여 이등변삼각형을 그리는 turtle 프로그램
# radian angle -> 60 way to angle (at natural position)
# 극좌표계 계산과 valueerror 방지를 위해 atan2 사용 (그렇게 흔한 버그는 아니니 acos로 사용)

import turtle
import math

wid = int(turtle.textinput("", "밑변 입력 : "))
hei = int(turtle.textinput("", "높이 입력 : "))

ang = math.degrees(math.acos((1/2 * (wid)) / pow (pow(hei, 2) + 1/4 * pow(wid, 2), 1/2)))
# ang = math.degrees(math.atan2(hei, wid/2))
betang = 180 - 2 * ang

turtle.goto(0,0)
turtle.fd(wid)
turtle.lt(180 - ang)
turtle.fd(math.sqrt(hei**2 + (wid/2)**2))
turtle.lt(180 - betang)
turtle.fd(math.sqrt(hei**2 + (wid/2)**2))

turtle.mainloop()
