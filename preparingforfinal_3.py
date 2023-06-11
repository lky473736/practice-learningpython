from tkinter import *

window = Tk()
color = "black"

def change_color_red():
    global color
    color = "red"

def change_color_blue():
    global color
    color = "blue"

def change_color_green():
    global color
    color = "green"

def exit_program():
    window.destroy()

def draw(event):
    x1, y1 = event.x - 1, event.y + 1
    x2, y2 = event.x - 1, event.y + 1
    canvas.create_oval(x1, y1, x2, y2, fill=color)

canvas = Canvas(window, height=300, width=300)
button_red = Button(window, text="r", command=change_color_red)
button_blue = Button(window, text="b", command=change_color_blue)
button_green = Button(window, text="g", command=change_color_green)
button_exit = Button(window, text="exit", command=exit_program)

canvas.pack()
button_red.pack()
button_blue.pack()
button_green.pack()
button_exit.pack()

canvas.bind("<B1-Motion>", draw)
window.mainloop()
