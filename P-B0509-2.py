'''class counter : 
    def __init__(self, i = 0) : # 값을 넣지 않았다면 0으로 처리
        self.count = i # 초기값 i
        
    def incre(self) : # 매소드
        self.count += 1

a = counter(100) 
a.incre()
print ("객체 a : ", a.count)'''

class hello : 
    def __init__ (self, saying = None) :
        self.saying = saying
        
    def sayhello (self, saying) :
        if saying :
            print ("hello!")
            
        else :
            print ("say anything")
            
p = input ("say anything to com : ")
h = hello ()

h.sayhello (p)