def getGrade (value) :
    if value >= 90 and value <= 100 : 
        return "A"
    
    elif value >= 80 and value < 90 :
        return "B"
    
    elif value >= 70 and value < 80 :
        return "C"
    
    elif value >= 60 and value < 70 :
        return "D"
    
    else : 
        return "F"
    
value = int(input("점수를 입력하세요 : "))
print ("점수는 ", getGrade(value), "입니다.")
