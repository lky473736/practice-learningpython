# list comprehension
# list 안에 수식이나 for문, 조건문을 넣어서 list의 component를 채워주는 고유 기능
# 참고 : https://butter-shower.tistory.com/205

before = [i+1 for i in range(10)]
after = [i+1 if i < 2 or i >= 8 else -i-1 for i in range(10)]

print (before)
print (after)