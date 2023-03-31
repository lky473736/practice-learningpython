# 임규연 (lky473736)
# 변수와 부등호, 조건, 반복문을 활용한 업다운 게임 

import random

number0 = random.randint(1,1000) # randint 함수를 사용 (컴퓨터가 숫자를 고르게 함)

print("컴퓨터는 1부터 1000까지 숫자 중 어느 하나를 택하였습니다.")

for i in range(10) : 
    print("남은 기회 : ", 10-i)
    number1 = int(input("10번의 기회로 숫자를 맞춰보세요. : ")) # 사용자 숫자 입력
    
    if number0 == number1 :
        print ("맞추셨습니다.")
        quit()
    
    elif number0 != number1 :
        if number0 > number1 :
            print ("up")
            
        elif number0 < number1 :
            print ("down")
            
print ("기회를 모두 소진하였습니다. 프로그램을 다시 실행해주세요.")
quit()