'''from tkinter import *
window = Tk()

def ftoc():
    pass

def ctof():
    pass
 
def exit():
    window.destroy()
    
l1 = Label(window, text="화씨")
l2 = Label(window, text="섭씨")
l1.grid(row=0, column=0) # grid : 표 만들기
l2.grid(row=1, column=0)

e1 = Entry(window)
e2 = Entry(window)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

btn1 = Button(window, text="화씨 -> 섭씨", command=ftoc)
btn2 = Button(window, text="섭씨 -> 화씨", command=ctof)
btn3 = Button(window, text="프로그램종료", command=exit)
btn1.grid(row=2, column=0)
btn2.grid(row=2, column=1)
btn3.grid(row=2, column=2)

window.mainloop()

# grid 배치는 아래와 같음
# 0 : "화씨" / 1 : 입력창 / 2 : "화씨 -> 섭씨"
# 0 : "섭씨" / 1 : 입력창 / 2 : "섭씨 -> 화씨"'''

# 밑변과 높이를 이용하여 이등변삼각형 출력하는 GUI
# https://github.com/lky473736/practice-learningpython/blob/dd915adff2ef0ed65d03ee3182188a2f638c5899/P-B0313-4.py#L34

import turtle
import math

from tkinter import *
window = Tk()

def go() :
    global wid, hei 
    
    wid = float(e1.get())
    hei = float(e2.get())
    
    drawtriangle()

l1 = Label(window, text = "밑변 입력")
l2 = Label(window, text = "높이 입력")
e1 = Entry(window)
e2 = Entry(window)
btn1 = Button(window, text = "실행", command = go)

l1.pack()
e1.pack()
l2.pack()
e2.pack()
btn1.pack()

def drawtriangle() :
    ang = math.degrees(math.acos((1/2 * (wid)) / pow (pow(hei, 2) + 1/4 * pow(wid, 2), 1/2)))
    # ang = math.degrees(math.atan2(hei, wid/2))
    betang = 180 - 2 * ang
    
    turtle.goto(0,0)
    turtle.fd(wid)
    turtle.lt(180 - ang)
    turtle.fd(math.sqrt(hei**2 + (wid/2)**2))
    turtle.lt(180 - betang)
    turtle.fd(math.sqrt(hei**2 + (wid/2)**2))

window.mainloop()
turtle.mainloop()