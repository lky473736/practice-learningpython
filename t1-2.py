# 임규연 (lky473736)
# turtle library를 이용한 행위예술 (random module을 사용해서)

import turtle
import random

t = turtle.Turtle()
r = random.Random()

t.shape("turtle")

while True :
    val1 = r.randint(0, 200)
    val2 = r.randint(0, 360)
    t.fd(val1)
    t.rt(val2)
    
t.mainloop()