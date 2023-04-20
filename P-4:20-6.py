a = [1, 2, 3, 4, 5, 0, 0]
b = [1, 3, 3, 4, 5, 6, 7]

samevaluelist = []

for i in range (len(b)) :
    if a[i] == b[i] :
        samevaluelist.append (a[i]) 
        

print (samevaluelist)