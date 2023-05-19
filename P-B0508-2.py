'''# dictionary {}
# key와 value가 있음 (자료를 찾을 때 key로 찾음 - value가 자료가 됨)
# 2차원 형태의 관계형 데이터베이스를 구성할 때 편리할 것임

adic = {"a" : 100, "b" : 200, "c" : 300}

print (adic["a"]) # a라는 key의 value를 출력

for i in adic :
    print (i, adic[i]) # key가 출력
    '''
    
# list : [] (요소 삭제, 추가, 값 변경 가능 / mutable)
# tuple : () (요소 추가 가능, 요소 삭제 및 값 변경 불가능)
# dictionary : {} (요소 삭제, 추가, value 변경 가능, 하지만 key는 값 변경 불가능)

sdic = {"모래두지" : 10,
        "핑복" : 5, 
        "삐" : 1,
        "파치리스" : 30}

print (sdic)

while True : 
    askkey = input ("어느 포켓몬의 수를 알려드릴까요? : ")
    
    match askkey :
        case "모래두지" :
            print (sdic["모래두지"])
            
        case "핑복" :
            print (sdic["핑복"])
            
        case "삐" :
            print (sdic["삐"])
            
        case "파치리스" :
            print (sdic["파치리스"])
            
        case _ :
            print ("프로그램을 종료합니다.")
            quit()