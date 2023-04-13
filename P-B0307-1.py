'''
# rad = int (input ("입력 = ")) # 입력받기 (input 겉에 껍질은 자료형에 따라 다름)
# int = interger

import math # 라이브러리 math 불러오기
# C : #include <math.h> (math 헤더파일 불러오기)
rad = 6
area = 3.14 * rad * rad # 영역 넓이
peri = 2 * 3.14 * rad # 영역 원주
print ("area = ", area)
print ("peri = ", peri)
print ("Math Rst = ", math.sin(math.radians(30)))
print(math.sqrt(10))
'''

# 등차수열의 합 계산기

coefficient = float(input("등차수열의 n의 계수 입력 : "))
constant = float(input("등차수열의 상수 입력 : "))
n = int(input("등차수열의 합의 n 입력 : "))

sum = n * (2 * (coefficient + constant) + (n - 1) * coefficient) / 2

print (sum)