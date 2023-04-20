studentDict = {}
keyList = []

n = int(input("counts? : "))

for i in range (n) : 
    key = input ("key? : ")
    value = input ("value? :")
    
    studentDict[key] = value
    keyList.append (key)
    
for i in range (n) :
    print ("Hi! I'm ", keyList[i], "and I'm from ", studentDict[keyList[i]])