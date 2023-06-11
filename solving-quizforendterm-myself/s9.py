import random

comnum = random.randint (1, 100)
chance = 7

for i in range (7) :
    mynum = int(input("n? : "))
    
    if mynum > comnum :
        print ("down")
    
    elif mynum < comnum :
        print ("up")
        
    else :
        print ("congratulation!")
        exit()
        
print ("lose")