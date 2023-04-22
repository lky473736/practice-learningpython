n = int(input("n의 값을 입력 : "))
sum = 0

for i in range (1, n + 1) :
    sum = sum + i**2
    
print (sum)