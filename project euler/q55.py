def palindromenumber(pn):
    p=str(pn)
    for x in range (len(p)):
        if p[x]!=p[-(x+1)]:
            return False
    return True

def addreverse(r):
    return int(str(r)[::-1])+r

def lchyrel(l):
    result=False
    g=addreverse(l)
    for x in range(1,51):
        if palindromenumber(g):
            return False
        else:
            result=True
        g=addreverse(g)
    return result




#print islychrelnumber(5)



f=0
for x in range(1,10000):
    if lchyrel(x):
        print x
        f+=1
print f

