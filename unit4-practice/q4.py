interger = int(input("정수를 입력 : "))

for i in range(1, interger + 1):
    if interger % i == 0 :
        print(i, end=' ')
        
print()