'''from tkinter import *

def mode1() :
    k = e1.get() 
    k = float(k)   
    print (k * (1.8) + 32)

def mode2() :
    j = e2.get() 
    j = float(j) 
    print ((j - 32) * 0.5)
    
def exit():
    window.destroy()
    
window = Tk()

l1 = Label(window, text="섭씨")
l2 = Label(window, text="화씨")
l1.pack() # pack : Tk에 해당되는 기능 집어넣기
l2.pack()

e1 = Entry(window) # Entry : 입력창
e2 = Entry(window)
e1.pack()
e2.pack()

btn1 = Button(window, text="섭씨 -> 화씨", command = mode1)
btn2 = Button(window, text="화씨 -> 섭씨", command = mode2)
btn3 = Button(window, text="프로그램종료", command=exit)
btn1.pack()
btn2.pack()
btn3.pack()

window.mainloop()'''

# 등차수열, 등비수열 계산기 GUI

from tkinter import *

window = Tk()

def arithmetic():
    a1 = float(e1.get())
    d = float(e2.get())
    n = float(e3.get())

    result = d * n + (a1 - d)
    e4.delete(0, END)
    e4.insert(0, result)

def geometric():
    a1 = float(e1.get())
    r = float(e2.get())
    n = float(e3.get())

    result = a1 * pow(r, (n - 1))
    e4.delete(0, END)
    e4.insert(0, result)

def calculatearithmetic() : 
    arithmetic()
    
def calculategeometric() :
    geometric()

def resetentry():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)

l1 = Label(window, text="초항")
l2 = Label(window, text="공차 / 공비")
l3 = Label(window, text="n?")
l4 = Label(window, text="결과")

e1 = Entry(window)
e2 = Entry(window)
e3 = Entry(window)
e4 = Entry(window)

btn1 = Button(window, text="등차수열 계산", command=calculatearithmetic)
btn2 = Button(window, text="등비수열 계산", command=calculategeometric)
btn3 = Button(window, text="초기화", command=resetentry)

# 초기 세팅: 등차수열
l1.grid(row=1, column=1)
l2.grid(row=1, column=2)
l3.grid(row=1, column=3)
l4.grid(row=1, column=4)

e1.grid(row=2, column=1)
e2.grid(row=2, column=2)
e3.grid(row=2, column=3)
e4.grid(row=2, column=4)

btn1.grid(row=3, column=1)
btn2.grid(row=3, column=2)
btn3.grid(row=3, column=3)

window.mainloop()
