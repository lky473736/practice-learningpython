# 임규연 (lky473736)
# 변수 2개 계산기 + 구구단 출력기 만들기

def calculator() : 
    val1 = float(input("첫번째 수를 입력해주세요 : "))
    val2 = float(input("두번째 수를 입력해주세요 : "))
    print("+ : 1 입력 / - : 2 입력 / * : 3 입력 / / : 4 입력")
    choice1 = int(input("연산자를 입력해주세요 : "))
    
    if choice1 == 1 : 
        print ("계산 결과 : ", val1+val2)
        
    elif choice1 == 2 :
        print ("계산 결과 : ", val1-val2)
    
    elif choice1 == 3 :
        print ("계산 결과 : ", val1*val2)
    
    elif choice1 == 4 :
        print ("계산 결과 : ", val1/val2)
        
    else : 
        print ("연산자를 잘못 입력하셨습니다. 프로그램을 다시 실행시켜주십시요.")
        quit()
    
def gugudan() :
    number = 0
    choice2 = int(input("몇단을 출력할까요? : "))
    
    for i in range (9) :
        number += 1
        print (choice2 * number)


print ("모드 : calculator or gugudan")
mode = input ("모드를 입력해주세요 : ")

if mode == "calculator" :
    calculator()
    
elif mode == "gugudan" :
    gugudan()
    
else : 
    print("프로그램을 종료합니다.")
    quit()