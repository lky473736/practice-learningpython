'''# list concatnation, comparison, copy 
# https://ko.wikipedia.org/wiki/%EB%AC%B8%EC%9E%90%EC%97%B4_%EC%97%B0%EA%B2%B0

lista = [1, 2, 3, 4, 5]
listb = [5, 6, 7, 8, 9]

listc = lista + listb # 중복이 되어도 중복된 거 그대로 표시 (합집합표현이랑 다름)

print ("-concatnation-")
print ('lista :', lista)
print ('listb :', listb)
print ('concatnation :', listc)
print ()

print ("-comparison-")
print ('lista * 5 =', lista * 5)
print (lista == listb) # 리스트 비교
print (lista != listb)
print (lista > listb) # 리스트에서 대소 : sum? 아니면 전체적인 평균?
print ()

# 복사의 종류 : 얕은 복사, 깊은 복사

print ("-thin copy-")
print ("original lista :", lista)
c_lista = lista # 리스트 전체를 복제
print ('copy lista thinly :', c_lista)
c_lista[0] = 'p'
c_lista[1] = 'k'
print ("thin copy of 'p', 'k' at position '0', '1' : ", c_lista) # 한 요소를 바꿈
print ()

print ("-deep copy-")
print ('original listb :', listb)
c_listb = list(listb) # 리스트 전체를 복제해서 다른 리스트를 새로히 만들어서 안에 요소로 넣음
print ('copy listb deeply :', c_listb)
c_listb[0] = 1
print (c_listb)'''

# https://wikidocs.net/16038
# https://velog.io/@kkamyang/Python-%EC%96%95%EC%9D%80-%EB%B3%B5%EC%82%AC-%EA%B9%8A%EC%9D%80-%EB%B3%B5%EC%82%AC-shallow-copy-deep-copy

# <concatnation : 조합, 결합 (리스트 끼리의 결합)>

import copy

alist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
blist = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

clist = alist + blist # concatnation
print (clist)

# <thin copy : 얕은 복사 (겉껍질만 복사 / 이중복사 금지)>

c_alist = alist.copy()
# list : mutable한 객체. 따라서 c_alist = alist와 같이 다른 변수에 할당하면 실제로는 같은 리스트 객체를 가리키게 됨.
# 따라서 copy 모듈을 이용해서 복사시켜주어야 함.
# 할당 != 복사

c_alist[0] = 'a'

print (alist)
print (c_alist)

dlist = [1, 2, [1, 2]]
tc_dlist = dlist.copy()

dlist[2].append(3) # dlist의 2번째 component list에 3 추가

print (dlist)
print (tc_dlist)
# 아마 둘의 리스트 안 2번째 component list에 3이 동시에 추가되었을 것이다.
# 이것이 얕은 복사의 정의다. 가장 겉 component에만 영향을 줄 수 있다.

# <deep copy : 깊은 복사 (안쪽 껍질에도 영향 o)>

dc_dlist = copy.deepcopy(dlist)

dlist[2].append(4)

print (dlist)
print (dc_dlist) 
# 이번에는 dlist에만 79번줄 코드가 작동되었다.