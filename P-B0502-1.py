'''import random

numbers = [10, 20, 30, 40, 50]
lista = ["ok", "rk", "pk", "nk"]

print ("랜덤 값 (in numbers) : ", random.choice(numbers))
print ("랜덤 값 (in lista) : ", random.choice(lista))

print ("합 = ", sum(numbers))
print ("최댓값 = ", max(numbers))
print ("최솟값 = ", min(numbers))'''

# 가위, 바위, 보

import random

rsp = ["가위", "바위", "보"]
com = random.choice(rsp)

choice = input ("가위, 바위, 보! : ")

print ("컴퓨터의 선택 : ", com)

if choice == com:
        print("비겼습니다!")
        
elif (
        (choice == '가위' and com == '보') or
        (choice == '바위' and com == '가위') or
        (choice == '보' and com == '바위')
    ):
        print("플레이어가 이겼습니다!")
        
else:
        print("컴퓨터가 이겼습니다!")