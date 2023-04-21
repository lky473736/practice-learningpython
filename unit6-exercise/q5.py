slist = []
equalthefirandend = 0

number = int(input("number? : "))

for i in range (number) :
    p = input("")
    slist.append(p)
    
for i in range (number) :
    if (slist[i])[0] == (slist[i])[-1] :
        equalthefirandend += 1
        
print (equalthefirandend)