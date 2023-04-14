'''
# 임규연 (lky473736)

# 변수의 세부 구현 사항 : 객체의 참조값(주소)
# 파이썬 : 객체 지향 언어 -> 변수나 클래스 등을 객체로 취급
# interpreter : id (변수) : 변수에 대한 객체아이디 출력 (컴퓨터에 따라 다르다)

x = int(input())
print (id(3))
print (id(x), "-->", x)

# 변수를 얉은복사할때 : 참조값의 복사
# 변수1 = 변수2 사용

# 변수를 깊은복사할때 : ?

# 불변객체 : 상수, 문자열, 튜플 (한번 만들어지면 변경 불가)
# 가변객체 : 변수, 리스트, 세트, 딕셔너리 (언제나 변경 가능한 객체)
'''

# 리스트와 배열은 다르다
# 리스트 : 다양한 형태를 넣을 수 있는 일종의 잡동사니 상자
# 배열 : 단 하나의 형태만 넣을 수 있는 정돈된 상자
# 파이썬에서는 리스트를 자주 사용한다

x = int(input("임의의 data 입력 : "))
print (id(x)) # id : 변수에 저장된 data의 고윳값

y = id(x)

print (id(y)) # id는 할당 연산자로 다른 변수를 정의하면 그 변수만의 고윳값으로 재지정된다