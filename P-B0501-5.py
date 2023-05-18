'''lists = [1, 2, 3, 4]

if 3 in lists : # 3이 리스트에 존재한다면
    lists.remove (3)
    
print(lists)

del lists[0] # remove랑 같음
print (lists)'''

# 홀수만 slist에 남기기

slist = []

for i in range (100) :
    slist.append (i + 1)

for k in slist :
    if k % 2 == 0 :
        slist.remove(k)
        
print (slist)