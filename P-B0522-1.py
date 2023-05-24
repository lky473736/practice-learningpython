'''# 단어 맞추기 게임 (사용자가 맞추지 못할 시에는 약간의 힌트를 줌)

import random # 컴퓨터가 단어를 랜덤으로 고를 수 있도록 random 라이브러리 사용
guess = "" # 단어를 맞추는 입력
tries = 10 # 단어를 맞출 수 있는 기회 

infile = open("/Users/alphastation/Desktop/컴퓨터공학전공/repository/learningpython/B0522-1.txt", "r")
lines = infile.readlines() # lines에는 infile에 있는 각각의 줄을 읽어서 각 요소를 리스트 형태로 저장되어 있음
print(lines)

word = random.choice(lines) # 컴퓨터가 고른 단어
word = word.rstrip() # rstrip : 문자열에 오른쪽 공백이나 인자가 된 문자열의 모든 조합을 제거 (여기선 개행 문자를 제거)

while tries > 0:
    failed = 0
    for char in word : # 컴퓨터가 고른 단어의 글자 
        # word = word.rstrip()
        if char in guess : # 사용자가 고른 단어의 글자 == 컴퓨터가 고른 단어의 글자
            print (char, end="") # 그 글자의 자리에 글자 표현
        else:
            print("_", end="") # 다른 자리에 _ 표현
            failed += 1 # 실패 횟수 추가
            
    if failed == 0 :
        print("사용자 승리") 
        break
    print("")
    
    in_char = input("단어 입력 : ") # 단어를 맞추는 입력
    guess += in_char # 위의 입력을 guess 안에 추가 (할당)
    
    if in_char not in word : # 컴퓨터가 고른 단어 != 내가 고른 단어
        tries -= 1
        print(str(tries) + "번 남았습니다.")
    if tries == 0:
        print("사용자 패배 정답은 " + word)
        
infile.close()'''

# 숫자 맞추기 게임 (경우의 수가 더 많아짐)

import random

tries = 20

infile = open("/Users/alphastation/Desktop/컴퓨터공학전공/repository/practice-learningpython/P-B0522-1.txt", "w+")

for i in range(1000):
    k = i + 1
    k = str(k)
    infile.write(k)
    infile.write("\n")

infile.seek(0)  # 파일의 읽기 위치는 0번째 줄로 놓음
showinfile = infile.readlines()
print(showinfile)

c = random.choice(showinfile)
com = [c]

while True:
    if tries == 0:
        print("기회를 다 소진하였습니다.")
        print("정답 : ", c)
        break

    choice = input("수를 입력하세요: ")

    if choice == c :
        print("맞추셨습니다. 프로그램을 종료합니다.")
        print("최종 기회 : ", tries)
        break

    else:
        print("틀렸습니다. 힌트를 드리겠습니다.")
        tries -= 1

        for i in range(len(choice)):
            if choice[i] == c[i]:
                print(choice[i], end="")
            else:
                print("_", end="")

        print("\n") 
