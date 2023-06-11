num = input("num? : ")

zeronum = 0

for i in range (len(num)) :
    if num[i] == "0" : 
        zeronum += 1
        
print (zeronum)