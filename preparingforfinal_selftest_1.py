# 1) 나 클래스 만들기 (변수 2개, 매소드 2개 이상)

class me : 
    def __init__ (self, age, height) :
        self.age = age
        self.height = height
        
    def printall (self) :
        print (self.age, self.height)
        
    def eatage (self) :
        self.age = self.age + 1 
        print ("나이가 들었습니다. 현재 나이 : ", self.age)
        
    def longer (self, height) :
        self.height = self.height + height
        print ("키가 커졌습니다. 현재 키 : ", self.height)
        
lgy = me (20, 178)
lgy.printall()

lgy.eatage()
lgy.printall()

lgy.longer(10)
lgy.printall()
