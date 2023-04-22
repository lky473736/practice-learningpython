def summation_sequence(n) :
    sum = 0
    for i in range (n) :
        sum = sum + ((i + 1) * 3)
    return sum
    
print ("3의 배수의 합 : ", summation_sequence(33))