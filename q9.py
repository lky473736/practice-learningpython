import turtle
turtle.shape ('arrow')

alist = [i for i in range (10, 130, 10)]

for i in range (0, len(alist)) :
    turtle.forward (alist[i])
    turtle.write (alist[i])
    turtle.backward (alist[i])
    turtle.right (30)
    
turtle.mainloop()