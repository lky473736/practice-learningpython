'''outfile = open("/Users/alphastation/Desktop/컴퓨터공학전공/repository/learningpython/B0516-3.txt", "w", encoding = "UTF-8")
# 인코딩을 선언하지 않으면 깨질 수 있음. 인코딩을 이용해서 포맷을 선언하기.
# 파일이 없으면 자기가 알아서 새로 생성해줌

for i in range (100) :
    i = str(i) # .write는 항상 str로 써줘야 함
    outfile.write (i)
    outfile.write ("\n")
    
outfile.close()'''

# n자릿수 원주율 계산기

infile = open ("/Users/alphastation/Desktop/컴퓨터공학전공/repository/practice-learningpython/P-B0516-3.txt", "w")

from decimal import *

def calculate_pi(n):
    getcontext().prec = n+1
    pi = Decimal(0)
    for k in range(n):
        pi += Decimal((-1)**k)/(1024**k)*(Decimal(256)/(10*k+1)+Decimal(1)/(10*k+9)-Decimal(64)/(10*k+3)-Decimal(32)/(4*k+1)-Decimal(4)/(10*k+5)-Decimal(4)/(10*k+7)-Decimal(1)/(4*k+3))
    pi = pi * 1/(2**6)
    return pi

n = int(input("원주율의 몇 번째 자릿수까지 계산할까요? "))
print("계산된 원주율:", calculate_pi(n))

infile.write (str(calculate_pi(n)))