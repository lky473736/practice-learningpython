list1 = []
list2 = []

while True :
    component_1 = input("list1 component 입력 (그만 입력하려면 q) : ")
    if component_1 == 'q' :
        break
    list1.append(component_1)
    
while True : 
    component_2 = input("list2 component 입력 (그만 입력하려면 q) : ")
    if component_2 == 'q' :
        break
    list2.append(component_2)
    
print (list1, len(list1))
print (list2, len(list2))
    
for i, (item1, item2) in enumerate(zip(list1, list2)) :
    if item1 == item2 :
        print(f'두 리스트의 {i+1}번째 원소인 {item1}은(는) 두 리스트에 모두 포함됩니다.')
    else :
        print(f'두 리스트의 {i+1}번째 원소 중 {item1}은(는) list1에만, {item2}는(은) list2에만 포함됩니다.')

if len(list1) != len(list2) :
    diff = abs(len(list1) - len(list2))
    print(f'두 리스트의 길이가 다릅니다. 길이 차이: {diff}')
    if len(list1) < len(list2) :
        print(f'list1은 list2보다 {diff}개의 원소가 적습니다.')
    else :
        print(f'list2은 list1보다 {diff}개의 원소가 적습니다.')
