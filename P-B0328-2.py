'''import turtle

t = turtle.Turtle()
t.shape("turtle")

n = int(input("각도 입력 : "))
l = int(input("길이 입력 : "))


# n각형 만들기
for i in range(n):
        t.fd(l)
        t.left(360/n)

t.penup
t.fd(l+100)
t.pendown()

for i in range(n+1):
        t.fd(l)
        t.left(360/(n+1))

t.penup
t.fd(l+100)
t.pendown()

for i in range(n+2):
        t.fd(l)
        t.left(360/(n+2))

t.penup
t.fd(l+100)
t.pendown()
        
turtle.mainloop()'''

# upgrade : 가상평면 (가상행렬)에서의 n각형
# turtle 드로잉 이슈 : in _incrementudc rasise Terminator -> 해결책 x, 코드 우회 필요

import turtle

numangle = int(turtle.textinput("", "number of angle?"))

if numangle > 0 :
        len = float(turtle.textinput("", "len?"))
        
        turnangle = 360 - ((180 / numangle) * ((numangle - 2) * numangle))
        
        for i in range (numangle) :
                turtle.forward (len)
                turtle.left (turnangle)
        
elif numangle == 0 :
        rad = float(turtle.textinput("", "rad?"))
        
        turtle.circle (rad)
        
        
turtle.getscreen()._root.destroy()
print ("Exit...")