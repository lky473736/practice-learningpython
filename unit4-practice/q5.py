n = int(input("정수를 입력 : "))

for i in range (n + 1) :
    for j in range (i) :
        print (j + 1, end = " ")
        
    print (" ")