'''
# # : 주석
# """ : 따옴표 세개 안에 있는 것 : 전체 주석

print ("화씨 및 섭씨온도 변환")

# def : 함수 지정 (반환값을 하나만 가질 수 있음) 
# 반환값을 여러가지 가지고 싶다면 포인터를 사용할 수 있음 

def function1 () : 
        ftemp = str(input("화씨온도 : "))
        ftemp = int(ftemp)
        ctemp = (ftemp-32.0)*5.0/9.0
        print ("섭씨온도 :", ctemp)
        
def function2 () :
        ctemp = str(input("섭씨온도 : "))
        ctemp = int(ctemp)
        ftemp = ctemp*1.8 + 32
        print ("화씨온도 :", ftemp)

while True:  # = while True : 무한정 반복하기 (= for i in range(True))
    
    selection = int (input("화씨면 1, 섭씨면 2 : ")) 
    
    if selection == 1 : # 조건문 사용하여 선택지 갈림길 만들기
        function1()

    elif selection == 2 : 
        function2()
    
    else :
        print ("선택번호 잘못됨.")
        break
    
    # 참고 : https://blockdmask.tistory.com/440
'''

# def와 조건문을 이용한 입력값 중 가장 큰 수 불러오기, 그에 해당되는 alphabet 구하기

numberofinput = int(input("수를 몇번 입력할 것인가요? : "))

alphabetlist = ['a', 'b', 'c', 'd', 'e', 'f', 
                 'g', 'h', 'i', 'j', 'k', 'l', 
                 'm', 'n', 'o', 'p', 'q', 'r', 
                 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

variablelist_alphabet = [] # 변수에 할당될 알파벳 리스트
variablelist_number = [] # 변수에 할당될 숫자 리스트 
z = 0 # 수 입력

copy_variablelist_number = []
matchingalphabet = ''

if numberofinput > 0 and numberofinput <= 26 :
    for i in range (numberofinput) :
        print ("현재 입력 횟수 : ", i)
        print ("앞으로의 입력 횟수 : ", numberofinput - (i))
        variablelist_alphabet.append (alphabetlist[i])
        z = float(input("수를 입력하세요. : "))
        variablelist_number.append(z)
        
    print (variablelist_alphabet)
    print (variablelist_number)
    
    copy_variablelist_number = variablelist_number # 복사본을 만들어둬서 alphabet과 matching
    
    variablelist_number.sort()
    biggestnumber = variablelist_number[-1]
    
    for j in range (numberofinput) : # matching
        if variablelist_number[-1] == copy_variablelist_number[j] :
            matchingalphabet = variablelist_alphabet[j]
    
    print ("따라서, 가장 큰 수는 ", str(biggestnumber),"입니다.")
    print ("이에 할당된 alphabet은 ", str(matchingalphabet), "입니다.")
    
else :
    print ("ERROR : 수의 범위에 어긋난 입력값입니다. 프로그램을 종료합니다.")
    quit()