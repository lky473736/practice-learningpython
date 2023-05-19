'''class tv : 
    ok = 500 # class members : ok
    
    def __init__ (self, chan = 10, vol = 10, state = "on") :
        self.chan = chan
        self.vol = vol
        self.state = state
        self.ok = tv.ok * 5 # tv.ok = 500
        # class members는 class이름.variable이름 으로 구성된다.
        
    def show (self) :
        print (self.chan, self.vol, self.state, self.ok)
        
tv1 = tv()
tv1.show()

def silent(obj) : # 객체를 함수로 전달
    obj.vol = 1
    
def louder(obj) : # 객체를 함수로 전달
    obj.vol = 20
    
silent(tv1)
tv1.show()

louder(tv1)
tv1.show()'''

# class members (class variable) : 모든 객체를 통틀어서 하나만 생성되고 모든 객체가 이것을 공유하는 변수
# 지역변수 (instance variable) vs class에서 전역변수 (class members)
# class members는 항상 class에서 선언하게 된다 (위의 ok 참고)

class radio : 
    def __init__ (self, setting = 'am', chan = 95, vol = 10, state = 'on') : 
        self.setting = setting
        self.chan = chan
        self.vol = vol
        self.state = state
        
    def printall (self) :
        print ("setting : ", self.setting)
        print ("chan : ", self.chan)
        print ("vol : ", self.vol)
        print ("state : ", self.state)
        
def settingchange (obj) : 
    if obj.setting == 'am' :
        obj.setting = 'fm'
    
    else : 
        obj.setting = 'am'
        
def chanchange (obj) :
    whatchan = int(input("what channel? : "))
    obj.chan = whatchan

def volchange (obj) : 
    whatvol = int(input("what vol? : "))
    obj.vol = whatvol
    
def statechange (obj) :
    if obj.state == 'on' :
        obj.state = 'off'
    
    else : 
        obj.state = 'off'
        

sradio = radio ()

while True : 
    print ()
    sradio.printall()
    
    print ("mode : setting, chan, vol, state (changable)")
    mode = input("input what you want to change (if you want quitting, input 0) : ")
    
    match mode : 
        case 'setting' : 
            settingchange (sradio)
        
        case 'chan' : 
            chanchange (sradio) 
            
        case 'vol' : 
            volchange (sradio)
            
        case 'state' :
            statechange (sradio)
            
        case '0' :
            print ("quitting")
            quit()
            
        case _ :
            quit()