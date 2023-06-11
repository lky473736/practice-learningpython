stacklist = []

while True :
    print (stacklist)
    mode = int(input("input the mode (1 : append, 2 : pop, 3 : exit) : "))
    
    match (mode) : 
        case 1 :
            appendcomponent = input("component? : ")
            stacklist.append(appendcomponent)
            
        case 2 :
            stacklist.pop()
            
        case 3 :
            exit()