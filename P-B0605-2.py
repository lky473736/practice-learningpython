'''# def : 일반함수
# lambda formula : 람다함수

# 1 일반함수로 표현

def celsius (t) :
    return (5.0 / 9.0) * (t - 32.0)

ftemp = [x * 10 for x in range(6)]

ctemp = list(map(celsius, ftemp))

print (ctemp)

# 2 lambda formula로 표현

ftemp = [x * 10 for x in range(6)]
ctemp = []

for i in ftemp :
    ct = lambda x : (5.0 / 9.0) * (x - 32.0) 
    ctemp.append (ct(i)) 

print (ctemp)'''

# lambda formula를 이용하여 일차식 계산기 만들기
# https://www.codeit.kr/community/questions/UXVlc3Rpb246NWUzNDUyMjU4MGU1MTMzNzNkOTYxMjYy
# https://wikidocs.net/30

slist = [] # 사용자가 추가한 component를 여기에
glist = [] # formula로 계산한 결과를 여기에

while True :
    try : 
        print (slist)
        k = int(input("component? (int / stop at input notthing) : "))
        
    except :
        break
    
    slist.append (k)
    
formula = input("input formula using x : ")

rst = lambda x : eval(formula)

for i in slist : 
    glist.append (rst(i))
    
print (glist)