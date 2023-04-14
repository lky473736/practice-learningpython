'''
# 별까지의 거리 계산하기

# dist = 40000000 # 실체 거리 : 상수 : 거리니깐 변할 수 있다
speed = 300000 # 실체 속도 : 상수 : 불변

dist = int(input("거리 : ")) # dist라는 변수에 정수형의 값을 입력받는다 -> 입력받은 값은 변수에 저장한다
r_dist = dist / speed
si = r_dist // 3600 # 60*60
bun = (r_dist - (si*3600)) // 60
cho = r_dist%60 # 나머지 (modular)
print (r_dist, "은", bun, "분", cho, "초")
print (r_dist, "은", si, "시", bun, "분", cho, "초")
'''

# 10진수의 n의 자리에 존재하는 0의 갯수 counting

val = input("10진수를 입력하시오. : ") # input example) val = 100

numberlist = []
whilecountingnumber = 0
zeronumber = 0

for i in range (len(val)) : # len(val) = 3
    numberlist.append (val[i])

print ("numberlist : ", numberlist)
print ("입력값의 길이 : ", len(val))

while whilecountingnumber < len(val) :    
    if numberlist[whilecountingnumber] == '0' : # 리스트를 차례대로 탐색하면서 0 찾음
        zeronumber = zeronumber + 1
        
    whilecountingnumber = whilecountingnumber + 1
    
print ("0의 갯수 : ", zeronumber)