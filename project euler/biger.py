def biger(factor):
    f=0
    for x in range(1,factor+1):
        if factor%x==0:
            f+=1
    return f
h=0
for x in range(1,10001):
    g=biger(x)
    if h<g:
        d=x
        h=g
print d
            
        