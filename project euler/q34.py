def j(x):
    h=1
    for y in range(1,x+1):
        h*=y
    return h
print j(0)

def c(y):
    g=0
    v=1
    for x in (str(y)):
        v=j(int(x))
        g+=v
    return g==y
p=0
for x in range(1,10000001):
    if c(x):
        print x

