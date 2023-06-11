slist = [1, 1]

n = int(input("n? : "))
for i in range (n) :
    if i > 1 :
        p = slist[i - 2] + slist[i - 1]
        slist.append (p)

print ("sum : ", sum(slist))
print ("nth : ", slist[-1])