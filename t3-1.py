# 임규연 (lky473736)
# color 값, rad 값 입력받아 circle 그리기

import turtle

in1 = turtle.textinput("", "원하는 color를 입력하세요.")
in2 = turtle.textinput("", "원하는 rad값을 입력하세요.")

in2 = int(in2)
turtle.color(in1)
turtle.circle(in2)

in2 = str(in2)

displaying = "color : " + in1 + ", rad : " + in2

turtle.write(displaying, font=("Arial", 16, "normal"))
turtle.mainloop()