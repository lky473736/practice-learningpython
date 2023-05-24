'''from tkinter import * # * = 모든 것

# "안녕! 반가워~"를 출력하는 함수
def hel():
    print("안녕! 반가워~")

# "잘가~"를 출력하는 함수
def bye():
    print("잘가~")

# 프로그램을 종료하는 함수
def exit():
    window.destroy() # window 자체가 Tk (Tkinter) 창 인스턴스를 의미. 따라서 window.destroy()는 quit과 같음

# Tkinter 창 인스턴스 생성
window = Tk()

# 버튼 위젯 생성과 해당 버튼이 클릭되었을 때 실행될 함수 설정
btn1 = Button(window, text="처음 인사", command=hel)
btn2 = Button(window, text="작별 인사", command=bye)
btn3 = Button(window, text="프로그램 종료", command=exit)
# 버튼 만들기 : a = Button (Tk창 인스턴스, text = "~~", command = 함수명)

# 버튼을 창에 배치
btn1.pack()
btn2.pack()
btn3.pack()

# 이벤트 루프 실행하여 창을 유지
window.mainloop()'''

# tkinter로 계산기 만들어보기

from tkinter import *
window = Tk()

def plus() :
    k = float(e1.get())
    j = float(e2.get())
    print (k + j)

def minus() :
    k = float(e1.get())
    j = float(e2.get())
    print (k - j)
    
def multi() :
    k = float(e1.get())
    j = float(e2.get())
    print (k * j)

def divide() :
    k = float(e1.get())
    j = float(e2.get())
    print (k / j)
    
e1 = Entry (window, bg = "lightgray")
e2 = Entry (window, bg = "lightgray")

e1.pack()
e2.pack()

bt1 = Button (window, text = "덧셈", command = plus)
bt2 = Button (window, text = "뺄셈", command = minus)
bt3 = Button (window, text = "곱셈", command = multi)
bt4 = Button (window, text = "나눗셈", command = divide)

bt1.pack()
bt2.pack()
bt3.pack()
bt4.pack()

window.mainloop()