'''lists = ['a', 'b', 'c', 'd']
print (lists)

lists.append ('k')
print (lists)

lists.remove ('k')
print (lists)

print (lists[0])

# 리스트 내 자료에 접근 : 리스트명[자리수]
# lists = ['a', 'b', 'c', 'd']
#           0    1    2    3

for i in lists : # 리스트 안에서의 반복문. 여기서 i는 lists[i]랑 동일한 말이 된다.
    print (i, end = " ") # end = " " : 큰따옴표 안에 있는게 출력하는 끝머리에 붙음
    
print (" ")'''

# for ~ in ~ 이용해서 0~99까지의 등차수열 n 출력기 만들기

nlist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range (1) :
    for j in nlist :
        for k in nlist :
            number = i * 100 + j * 10 + k
            print (number)

