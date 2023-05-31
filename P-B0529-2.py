'''# 메모장 만들기

from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

window = Tk()
text = Text(window, height = 30, width = 80)
text.pack()

def open() : # 파일 열기
    file = filedialog.askopenfile(parent = window, mode = 'r') # 파일 탐색 후 열기기능
    if file != None : # 파일이 비어있지 않다면 (용량이 있다면)
        lines = file.read() # 파일 읽기
        text.insert('1.0', lines) # 1.0 : 줄간격, window에 텍스트 넣기
        file.close()
    
def save() :
    file = filedialog.asksavefile(parent = window, mode = 'w') # 파일 탐색 후 저장기능
    if file != None : # 파일이 비어있지 않다면 (용량이 있다면)
        lines = text.get('1.0', END+'-1c') # 파일 쓰기
        file.write(lines)
        file.close()
    
def saveandexit() :
    if messagebox.askokcancel("Quit", "종료하시겠습니까?") : # 종료할지 묻는 박스
        window.destroy()

def about() :
    label = messagebox.showinfo ("About", "메모장 프로그램") # 메세지 박스가 뜸 (About : 창 이름)

menu = Menu (window) # 상단 표시줄 만들기
window.config(menu = menu)

filemenu = Menu (menu)
menu.add_cascade(label = "파일", menu = filemenu) # 메뉴의 이름 짓기
filemenu.add_command(label = "열기", command = open)
filemenu.add_command(label = "저장하기", command = save)

helpmenu = Menu (menu)
menu.add_cascade(label = "도움말", menu = helpmenu)
helpmenu.add_command(label = "프로그램 정보", command = about) # 메뉴 안 커맨드 만들기

exitmenu = Menu (menu)
menu.add_cascade(label = "시스템", menu = exitmenu) # 종료
exitmenu.add_command(label = "종료", command = exit)

window.mainloop()'''

# 간절한 소원은 이루어진다
# tkinter에서 메모장을 구현해서 사용자에게 6개의 숫자를 입력받고, 복권 시스템 구축
# 그 중 랜덤으로 4개 이상의 숫자가 맞을 수 있도록 구현함

import os # os 라이브러리를 이용해서 파일이 존재하는지 여부를 물을 것임
import time # time 라이브러리를 이용해서 infinite loopstation에서 걸리는 overflow를 최소화할거임
import random
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

window = Tk()
text = Text(window, height = 30, width = 80)
text.pack()

rlist = []
nlist = []
file_path = "/Users/alphastation/Desktop/repository/practice-learningpython/lotto.txt"
    
def saveandexit() :
    file = filedialog.asksaveasfile(parent = window, mode = 'w') # 파일 탐색 후 저장기능
    if file != None : # 파일이 비어있지 않다면 (용량이 있다면)
        lines = text.get('1.0', END+'-1c') # 1.0 : 줄간격, -1c : 개행 문자 제거
        file.write(lines)
        file.close()

def about() :
    label = messagebox.showinfo ("About", "간절한 소원은 이루어진다") # 메세지 박스가 뜸 (About : 창 이름)

'''while True:
    if check_file():
        break

    time.sleep(1)

window.mainloop()''' # while을 통하여 사용자의 응답을 대기할 경우 blocking 현상 때문에 렉이 걸림. 따라서 after를 사용하는 것임

def check_file():
    global nlist
    nlist = []
    if os.path.exists(file_path):
        with open(file_path, 'r') as infile:
            infilelines = infile.readlines()

        # 파일 내용 출력
        for line in infilelines:
            line = line.rstrip('\n')  # 개행 문자 제거
            nlist.append(line)

        print(nlist)
        lottery()
        
    else :
        window.after(1000, check_file)

def lottery() :
    global rlist
    global nlist
    rlist = []
    
    print("복권 추첨을 시작합니다.")
    
    while len(rlist) < 5 :
        choose = int(random.choice(nlist))
        
        if choose not in rlist :
            rlist.append(choose)
            print ("%d번째 숫자 뽑았습니다." %len(rlist))
            
    while len(rlist) < 6 :
        choose = random.randint(1, 45)
        
        if choose not in rlist :
            rlist.append(choose)
            print ("%d번째 숫자 뽑았습니다." %len(rlist))
            
    print("이제, 복권 숫자를 공개하겠습니다! 카운트다운!")
    for i in range(5):
        print(5 - i)
        time.sleep(1)
        
    rlist.sort()
    print("축하드립니다!")
    print(rlist)
    
    print ("중복되는 4개의 수")
    for i in range (len(rlist)) :
        if rlist[i] in nlist :
            print (rlist[i])
    
    exit()
    
def main():
    menu = Menu(window)
    window.config(menu=menu)

    label = messagebox.showinfo("About", "파일은 repository에 저장하고, 이름은 lotto.txt로 저장하십시요.")

    menumenu = Menu(menu)
    menu.add_cascade(label="메뉴", menu=menumenu)
    menumenu.add_command(label="프로그램 정보", command=about)
    menumenu.add_command(label="숫자 작성 완료", command=saveandexit)

    check_file()
    window.mainloop()


if __name__ == "__main__":
    main()