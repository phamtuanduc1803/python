import operator
l=[]
while True:
    s = raw_input()
    if not s:
        break
    l.append(tuple(s.split(",")))
print sorted(l,key=operator.itemgetter(0,1,2))
