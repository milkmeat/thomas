import math
def ygs(g):
    s=0
    for x in range (2,int(math.sqrt(g))):
        if g%x==0:
            s=s+2
    return s
def tri(h):
    f=0
    for d in range (1,h+1):
        f=f+d
    return f
print tri(100)            
for x in range (1,1000000):
    b=ygs(tri(x))
    if b>=500:
        print tri(x)
        break
 