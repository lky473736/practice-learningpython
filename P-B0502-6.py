'''stuple = (0, 1, 2, 3)
stuple += (0, 1) # component concatnate

print (stuple)

# 리스트 : 딕셔너리에서 키로 이용 x (계속 바뀔 수 있으니깐)
# 튜플 : 딕셔너리에서 키로 이용 o (바꿀 수 없으니깐)'''

# tuple은 이미 정해진 값의 변경이 불가능한 것 뿐이지 추가는 가능하다. 
# 하지만 pop, remove, del (삭제)는 불가능하다.

stuple = (0, 1, 2, 3)
stuple += (0, 1) # +=을 이용한 요소 추가 : component concatnate

print (stuple)