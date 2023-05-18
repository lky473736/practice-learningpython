'''lists = [0, 1, 2, 3, 4, 5, 6]

print (lists.index(3)) # index : 괄호 안에 있는 원소가 몇 번째 원소인지 나타냄
del lists[2]
print (lists)'''

import time

slist = [i + 1 for i in range (100)]

for k in range (len(slist)) :
    print (slist)
    del slist[k]
    time.sleep(1)