slist = []

number = int(input("입력할 값의 갯수 : "))

for i in range (number) :
    a = int(input())
    slist.append(a)
    
print ("값의 합계 : ", sum(slist))