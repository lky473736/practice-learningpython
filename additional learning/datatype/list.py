global slist 
slist = [0, 1, 4, 3, 2]

# 리스트 또한 인덱싱과 슬라이싱 가능

# del 사용 시엔 인덱싱 혹은 슬라이싱한 객체만 가능

# sort : 오름차순 정렬
slist.sort()
print (slist)

# sort (reverse = True) : 내림차순 정렬
slist.sort(reverse=True)
print (slist)

# reverse : 뒤집기 (원래 있던 형태에서 뒤집기)
slist.reverse()
print (slist)

# extend = list concatnate
alist = [1, 2]
blist = [3, 4, 5, 6]

clist = alist + blist
print (clist)

clist.extend([7, 8, 9])
print (clist)