paper = open ("/Users/alphastation/Desktop/repository/practice-learningpython/solving-quizforendterm-myself/word.txt", "r")
lines = paper.readlines()

for i in range (len(lines)) :
    k = lines[i].strip()
    lines[i] = k

print(lines)

slist = []

for j in lines :
    if len(j) > 5 : 
        slist.append (j)

print (slist)