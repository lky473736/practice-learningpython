# 임규연 (lky473736)
# 키보드로 움직임 제어하기

# 직교좌표계 상에서 움직이는 터틀을 표현
# left 키 : 왼쪽으로 30도 각도 틀기
# right 키 : 오른쪽으로 30도 각도 틀기
# 항상 앞으로 가고 있음

import turtle

t = turtle.Turtle()
t.shapesize(3, 1) # shapesize : comma를 기준으로 가로, 세로 순으로 n배 커짐
t.speed (3)

s = turtle.getscreen

def left() :
    t.lt(30)
    t.fd(30)
    
def right() :
    t.rt(30)
    t.fd(30)

s.onkeypress(left, "Left")
s.onkeypress(right, "Right")
    
turtle.mainloop()