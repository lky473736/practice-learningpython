print (abs (-18290813881239182938619286313))


print (all ([0, 2, 3])) # False
print (any ([0, 2, 3])) # True


formula = "3 + 1"
print (eval(formula))


slist = [1, 2, 3, 4]
print (sum(slist))


print (len(slist))


slist = tuple(slist)
print (slist)


print (max(slist))
print (min(slist))


def selfsum (x) :
    return x + x
slist = list(slist)
print (list(map(selfsum, slist)))


print (list(enumerate(slist)))


def condition (x) :
    return x > -1

print (list(filter(condition, slist)))


slist.sort (reverse=True)
print (slist)
