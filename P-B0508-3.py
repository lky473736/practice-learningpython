'''pbook = {}

pbook["홍길동"] = "010-1234-5678" # 홍길동이라는 key 생성, 거기에 value 입력

print (pbook["홍길동"]) # key를 이용한 value 검색

pbook["강감찬"] = "010-9876-5432"

print (pbook["강감찬"])

pbook["광개토대왕"] = "010-1928-3746"

print (pbook["광개토대왕"])

for i in pbook :
    print (i, pbook[i])
    
sear = input("검색 시스템 : key를 입력하세요. : ")
print (pbook[sear])'''

# dictionary에서 key와 value는 항상 같이 append 해야한다.

sdic = {}

sdic["대한민국"] = ["김치", "떡볶이", "불고기"]
sdic ["영국"] = ["피쉬 앤 칩스", "잉글리쉬 브랙퍼스트"]
sdic ["일본"] = ["낫또", "스시", "라멘"]

for i in sdic :
    print (i)
    
while True :
    sear = input ("어느 나라의 전통음식을 검색하시겠어요? : ")
    
    if sear in sdic : 
        print (sdic[sear])
        
    else : 
        print ("dict에 해당 나라가 없습니다. 프로그램을 종료합니다.")
        exit()