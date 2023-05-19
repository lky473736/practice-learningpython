'''scoredic = {"kim" : [99, 83, 95],
            "lee" : [68, 45, 78],
            "choi" : [25, 56, 69]}

for a, b in scoredic.items() : # 매개변수 2개를 이용한 반복문 (in item 필요)
    print (a, b)
    
for i in scoredic :
    print (i, "의 평균성적 = ", sum(scoredic[i]) / len(scoredic[i]))'''
    
sum = 0
number = 0
    
vegdic = {'potato' : 10002333982392328,
          'carrot' : 319716971639691376971,
          'onion' : 87197191637363766373676376373}
 
for a, b in vegdic.items() : # vegdic에 있는 각 component를 a, b로 지정 (dictionary에서만 items 가능)
    print (a, b)
    
for k in vegdic : 
    sum = sum + vegdic[k]
    number = number + 1
    
print ("총 갯수의 평균 : ", sum / number)