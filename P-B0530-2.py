'''class person :
    def __init__ (self, name, age) :
        self.name = name
        self.age = age
        
    def __repr__ (self) : # 객체를 문자열로 변환하여 반환
        return "<name : %s, age : %s>" %(self.name, self.age)
    
def kage (person) : # class를 instance한 함수 만들기
    return person.age

people = [person('lim', 20), person('daramji', 3)]

print (sorted(people, key = kage))'''

# __repr__의 의미
# 파이썬 클래스에서 객체를 문자열로 표현하는 데 사용

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"

person = Person("Alice", 25)
print(person)  

# 출력: Person(name='Alice', age=25)
# print 안에는 수식이나 변수, 문자열이 들어가야 하는데 여기서 repr를 사용해 객체를 문자열로 만들어줬기 때문에 출력이 가능한 거임
