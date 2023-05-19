'''class car :
    def __init__ (self, velocity, color, model) :
        self.velocity = velocity
        self.color = color
        self.model = model
        
    def printall (self) :
        print (self.velocity, self.color, self.model)
        
    def drive (self, a) :
        self.velocity = a # 매개변수 a를 써서 괄호 안에 수를 입력할 수 있게끔 함
        
    def move (self, p, r, q) :
        pass # 그냥 다음 코드 줄로 넘어가는 매소드
    
car = car(0, "silver", "sonata")

print (car.velocity)
print (car.color)
print (car.model)

car.printall()

car.drive (90)

car.printall()

# 클래스 내부의 함수 정의 (public, private)'''

# 할당 : 어떤 변수의 메모리에 특정 값, 특정 함수, 특정 변수를 동일하게 삽입
# 할당은 복사와 다르다

a = 1
b = 2

print (a, b)

a = b

print (a, b)