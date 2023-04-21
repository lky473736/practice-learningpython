a = [1, 2, 3, 4, 5]

b = [1, 3, 3, 4, 5, 6, 7]

slist = [a[i] for i in range (len(a)) if a[i] == b[i]]

print (a)
print (b)
print (slist)