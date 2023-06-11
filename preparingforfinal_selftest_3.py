# 3) 그림판 만들기

from tkinter import *
window = Tk()

color = "black"

def cred() :
    global color
    color = "red"
    
def cblue() :
    global color
    color = "blue"
    
def cgreen() :
    global color
    color = "green"
    
def exit() :
    window.destroy()
    
def paint (event) :
    x1, y1 = event.x-1, event.y+1
    x2, y2 = event.x-1, event.y+1
    canvas.create_oval (x1, y1, x2, y2, fill = color)
    
canvas = Canvas (window, height = 300, width = 300)
b1 = Button (window, text = "r", command = cred)
b2 = Button (window, text = "b", command = cblue)
b3 = Button (window, text = "g", command = cgreen)
b4 = Button (window, text = "exit", command = exit)

canvas.pack()
b1.pack()
b2.pack()
b3.pack()
b4.pack()

canvas.bind ("<B1-Motion>", paint)
window.mainloop()

# 왜 색상이 변하지 않지? => macos에서는 tkinter에서 색상 지원이 한정적이여서 색상 안변함