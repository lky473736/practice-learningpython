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

while True : 
    t.shape ("turtle") # turtle, arrow, circle ... 다양한 커서 모양을 가질 수 있다
    leng = int(input("길이 : ")) # 길이를 입력받는다
    print ("1 : 삼각형, 2 : 사각형, 3 : 원")
    choice = int(input("당신의 선택은? : "))
    t.clear() # 꼬부기가 그린거 지운다
    
    if choice == 1:
        triangle()
    
    elif choice == 2:
        square()
        
    elif choice == 3:
        t.circle(leng)
        
    else:
        print("프로그램 종료")
        break # 반복문 종료
    

turtle.mainloop()  
'''

# turtle와 random을 이용한 행위예술 ver.2

import turtle as t
import random 

t.colormode(255) # 3-tuple로 rgb 값 받기
t.speed (0)

def moverandomly(b) : # 움직임 함수
    t.goto(random.randint(-200, 200), random.randint(-200, 200))

def crazytriangle(a) : # 삼각형 그리기 (매개변수 a)
    for j in range (a) : 
        r = random.randint(1, 255)
        g = random.randint(1, 255)
        b = random.randint(1, 255)
        
        dir = random.randint(1, 2)
        len = random.randint(1, 200)
        
        t.write("%s, %s, %s" %(r, g, b)) # 삼각형 각각의 rgb 값 모니터에 출력
        
        t.pencolor(r, g, b)
        
        for i in range (3) :
            t.fd(len)
            if dir == 1 :
                t.rt(120)
            else :
                t.lt(120)
            
        t.penup()
        moverandomly(a)
        t.pendown()
        

val = int(t.textinput("", "삼각형 갯수 : "))

crazytriangle(val)

t.mainloop()