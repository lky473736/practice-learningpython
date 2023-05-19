'''items = {"레쓰비" : 10,
         "코카콜라" : 7,
         "포카칩" : 4,
         "사발면" : 120,
         "삼다수" : 1024}

print ("현재 재고")
for i in items :
    print (i, items[i])
    
mode = int(input("1은 재고 추가, 2는 검색 기능 : "))

if mode == 1 :
    while True :
        print ("그만 추가하려면 key에 0 입력")
        plus_itemkey = input("재고 key 이름 : ")
        
        if plus_itemkey == '0' :
            break
        
        plus_itemvalue = input("재고 수 : ")
        items[plus_itemkey] = plus_itemvalue
        
elif mode == 2 :
    while True :
        print ("그만 검색하려면 key에 0 입력")
        sear = input("key 입력 : ")
        if sear == '0' :
            break
        
        print (items[sear])'''
        
# dictionary를 이용하여 스타벅스 키오스크 시스템 구현

menu = ("drink", "bread", "etc")

drinklist = ['americano', 'latte', 'cappuccino', 'mocha', 'chocolate', 'macchiato']
breadlist = ['flatbread', 'honeybread', 'bagel', 'croissant']
etclist = ['icecream', 'affogato', 'soup']

buy = []

menudic = {menu[0] : drinklist, 
           menu[1] : breadlist, 
           menu[2] : etclist}

print ("안녕하세요! 여기는 스타벅스입니다.")

def drinksel() :
    print (menudic[menu[0]])
    
    while True : 
        dsel = input("어떤 음료를 주문하시겠어요? (만약 메뉴 추가를 중지하고 싶으시면 0을 입력하세요) : ")
        
        if dsel == '0' :
            break
        
        if dsel in drinklist :
            print ("정상적으로 추가되었습니다.")
            buy.append (dsel)
        
        else :
            print ("메뉴에 없는 제품입니다.")
            
def breadsel() :
    print (menudic[menu[1]])
    
    while True : 
        dsel = input("어떤 빵을 주문하시겠어요? (만약 메뉴 추가를 중지하고 싶으시면 0을 입력하세요) : ")
        
        if dsel == '0' :
            break
        
        if dsel in breadlist :
            print ("정상적으로 추가되었습니다.")
            buy.append (dsel)
        
        else :
            print ("메뉴에 없는 제품입니다.")
        
def etcsel() :
    print (menudic[menu[2]])
    
    while True : 
        dsel = input("어떤 메뉴를 주문하시겠어요? (만약 메뉴 추가를 중지하고 싶으시면 0을 입력하세요) : ")
        
        if dsel == '0' :
            break
    
        if dsel in etclist :
            print ("정상적으로 추가되었습니다.")
            buy.append (dsel)
        
        else :
            print ("메뉴에 없는 제품입니다.")
            
def drinkmaster() :
    while True : 
        print (menudic[menu[0]])
        
        a = int(input("0 : 추가 / 1 : 삭제 / 2 : 종료 : "))
        
        if a == 0 :
            b = input("추가할 메뉴 : ")
            drinklist.append(b)
            
        elif a == 1 :
            c = input("삭제할 메뉴 : ")
            drinklist.remove(c)
        
        else :
            break
        
def breadmaster() :
    while True : 
        print (menudic[menu[1]])
        
        a = int(input("0 : 추가 / 1 : 삭제 / 2 : 종료 : "))
        
        if a == 0 :
            b = input("추가할 메뉴 : ")
            breadlist.append(b)
            
        elif a == 1 :
            c = input("삭제할 메뉴 : ")
            breadlist.remove(c)
        
        else :
            break
        
def etcmaster() :
    while True : 
        print (menudic[menu[2]])
        
        a = int(input("0 : 추가 / 1 : 삭제 / 2 : 종료 : "))
        
        if a == 0 :
            b = input("추가할 메뉴 : ")
            etclist.append(b)
            
        elif a == 1 :
            c = input("삭제할 메뉴 : ")
            etclist.remove(c)
        
        else :
            break
            
def master () :
    print ("관리자 모드에 접속하였습니다.")
    
    while True : 
        print (menudic)
        mod = input("조정이 필요한 디렉토리 입력 (0 : 종료): ")
    
        match mod : 
            case '0' : 
                break
        
            case "drink" :
                drinkmaster()
        
            case "bread" :
                breadmaster()
            
            case "etc" :
                etcmaster()
                
            case _ :
                print ("디렉토리 입력이 잘못되었습니다. 프로그램을 종료합니다.")
                exit()
        

while True :
    print (menu)
    print ("현재 선택하신 메뉴 리스트는 다음과 같습니다. : ", buy)
    menusel = input("원하시는 디렉토리를 입력하세요! (만약 메뉴 추가를 중지하고 싶으시면 0을 입력하세요) : ")

    match menusel : 
        case '0' : 
            break
        
        case "drink" :
            drinksel()
        
        case "bread" :
            breadsel()
            
        case "etc" :
            etcsel()
            
        case "master" :
            master() 
            
        case _ :
            print ("디렉토리 입력이 잘못되었습니다. 프로그램을 종료합니다.")
            exit()
            
print ("선택하신 메뉴는 ", buy, "입니다.")
print ("감사합니다. 스타벅스였습니다!")