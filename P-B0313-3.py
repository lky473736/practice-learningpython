'''
#a = 10
#h = 10
#area = 10 * 10 / 2
#print (area)

wid = int (input("밑변 입력 : "))
hei = int (input("높이 입력 : "))

area = 1/2 * wid * hei
print ("삼각형의 면적은 ", area)
'''

# 직각삼각형의 빗변 구하기

from math import sqrt

a = float(input("fisrt value : "))
b = float(input("secound value : "))

c = sqrt(pow(a, 2) + pow(b, 2))

if a + b < c : # triangle rule
    print ("error : non-triangle rule")
    quit

print (c)