# 임규연 (lky473736)
 
'''
# 원리금 계산

a = int(input("원리금 : ")) 
r = float(input("이자율 : ")) # 이자율은 비율이기 때문에 float (실수, R) 형을 사용하여 입력받는다
n = int(input("기간 : "))

rst = a * (1 + r)** n # 지수는 **으로 표현함

print ("원리금 합계는 ", rst)
print ("원리금 합계는 = %.2f" %rst) # 소수점 두자리 수까지 표현

# %nf : 소수점 n자리 수까지 표현
# 파이썬 ppt 자료에 있는 우선 순위표 중요 (여러 번 회독하기)
'''

# 원주율 계산기

# 원주율 = 원의 둘레의 길이 / 원의 지름의 길이

from math import pi

doolle = int(input("지름의 길이 : "))

jirum = doolle / pi

print (jirum)

print (doolle / jirum) # pi 값 출력됨