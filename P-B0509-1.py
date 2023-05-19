'''# 객체, 클래스, tkinter, 파일

# 객체지향 조건
# 1) class가 만들져야 함
# 2) 상속
# 3) 캡슐화 (encapsulation)
# 4) 정보은닉
# 5) 다형성 (overwriting, overloading)

# SA/SD -> 절차 지향 프로그래밍 : procedure를 기반
# 객체 지향 프로그래밍 : 데이터와 함수를 한 덩어리로 묶어서 생각

# 객체 : attribute(변수형태), action(매소드형태)
# 클래스로부터 만들어지는 객체 : 인스턴스 (instance)

class counter : 
    def __init__(self) : # 생성자
        self.count = 0 # 초기 변수 세팅
        
    def incre(self) : # 매소드
        self.count += 1

a = counter() # a는 객체다 (instance -> class)
a.incre()
print ("객체 a : ", a.count)

b = counter()
b.incre()
print ("객체 b : ", b.count)
'''

'''
따로 공부한 걸 바탕으로 내 방식대로 객체지향을 자세히 기술하자면 다음과 같다.

일단 객체 (object)가 뭐냐면 하나의 이름표이다. 
주제가 전부 동일한 함수 및 매소드들을 여러 개 만든 다음 그걸 class라는 통에 담고,
그 통에 이름표를 붙여주는 것이 객체라고 보면 쉽다.

예를 들어서 아래와 같이 표현할 수 있다.
'''

class sclass : # sclass라는 class를 만듦
    def __init__ (self, a, b) : # sclass의 초기 설정자 (생성자)
        self.a = a # 초기 변수를 세팅
        self.b = b
        
sobject = sclass (3, 4) # sclass의 초기 변수 설정을 a = 3, b = 4로 놓고 sclass라는 통에 sobject라는 이름을 붙임

''' 
따라서 sclass에 sobject라는 객체, 즉 이름이 생겼으니 우리는 sobject.~(~)라고 표현할 수 있다. 
class와 그에 따른 객체를 만들 수 있는 언어를 객체지향 언어라고 하며, python은 객체지향 언어이기도 하고 절차지향 언어이기도 하면서, 함수형 언어이기도 하면서... 그냥 짬뽕된 언어다.

객체지향 언어엔 5가지의 조건이 있는데 이는 아래와 같다.

1) class를 생성할 수 있어야 한다 : 당연히 class가 있어야 거기에 객체를 생성해낼 수 있으니 class가 없으면 객체지향이 아니다.
2) 상속 : http://www.tcpschool.com/java/java_inheritance_concept 참고
3) 캡슐화 : https://bperhaps.tistory.com/entry/%EC%BA%A1%EC%8A%90%ED%99%94%EB%9E%80-%EB%AC%B4%EC%97%87%EC%9D%B8%EA%B0%80-%EC%96%B4%EB%96%A4-%EC%9D%B4%EC%A0%90%EC%9D%B4-%EC%9E%88%EB%8A%94%EA%B0%80 참고
4) 정보은닉 : 변수를 public, private 할 수 있는가를 말하는 것이다.
5) 다형성 : https://88240.tistory.com/228 참고

객체지향 언어는 Java가 대표적이니 그때 가서 정확히 배워야겠다.
'''