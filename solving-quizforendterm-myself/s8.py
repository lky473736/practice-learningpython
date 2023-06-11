# s6~s7 : 건너뜀 

parentnum = 0
childnum = 0

for i in range (6) :
    for j in range (6) :
        for k in range (6) :
            if (i + 1) % 2 != 0 and (j + 1) % 2 != 0 and (k + 1) % 2 != 0 :
                childnum += 1
            
            parentnum += 1
    
print (childnum)
print (parentnum)
print (childnum / parentnum)
