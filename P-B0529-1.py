'''# 그림판 만들기

from tkinter import *
window = Tk()

color = "blue"

def cred() :
    global color # 지역변수로 만들어서 빨간색으로 만들거임
    color = "red"
    
def cgreen() :
    global color 
    color = "green"
    
def cblue() :
    global color
    color = "blue"
    
def end() :
    exit()
    # == window.destroy()
    
def paint(event) : 
    x1, y1 = (event.x-1), (event.y+1)
    x2, y2 = (event.x-1), (event.y+1)
    canvas.create_oval (x1, y1, x2, y2, fill = color)

canvas = Canvas(window, height = 500, width = 500)
canvas.pack()

b1 = Button(window, text = "빨강색", command = cred)
b1.pack()

b2 = Button(window, text = "초록색", command = cgreen)
b2.pack()

b3 = Button(window, text = "파란색", command = cblue)
b3.pack()

b4 = Button(window, text = "종료", command = end)
b4.pack()

canvas.bind("<B1-Motion>", paint)
window.mainloop()'''

# 그림판의 원리 이해하기
# 마우스를 가져다 댄다 -> 자취가 생긴다 -> 그 자취에 점을 찍는다

from tkinter import *
window = Tk() # Tk 클래스로 통해 window라는 instance 생성 (window = object)

color = "blue" # 처음엔 blue로 설정 

def cred() :
    global color # 지역변수로 만들어서 빨간색으로 만들거임
    color = "red"
    
def cgreen() :
    global color 
    color = "green"
    
def cblue() :
    global color
    color = "blue"
    
def end() :
    exit()
    # == window.destroy()
    
def paint(event) : # 마우스 이벤트인 <B1-Motion>이 발생할 때 paint 함수 실행됨
    global color
    # 왜 x1, y1, x2, y2 이렇게 변수가 4개인가? -> 점을 확대하면 원이다. window에 작은 원을 그려 paint 표현할 것임
    x1, y1 = (event.x-1), (event.y+1) # 좌상단 모서리 좌표의 위치 세팅
    x2, y2 = (event.x-1), (event.y+1) # 우상단 모서리 좌표의 위치 세팅
    # (event.x-1), (event.y+1) : 원을 매끄럽게 그리기 위한 수식 (일종의 전처리 과정)
    canvas.create_oval (x1, y1, x2, y2, fill = color) # 원을 그림 + 원에 color 채워넣음

canvas = Canvas(window, height = 500, width = 500)
canvas.pack()

b1 = Button(window, text = "빨강색", command = cred)
b1.pack()

b2 = Button(window, text = "초록색", command = cgreen)
b2.pack()

b3 = Button(window, text = "파란색", command = cblue)
b3.pack()

b4 = Button(window, text = "종료", command = end)
b4.pack()

canvas.bind("<B1-Motion>", paint)
window.mainloop()

# 문제 : 색깔이 변경되지 않음 : https://stackoverflow.com/questions/67370694/tkinter-create-oval-method-does-not-change-color
# 그래도 색깔이 변경되지 않음