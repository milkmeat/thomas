import math

def ygs(g):
    s=2  # 1 and itself
    for x in range (2, int(math.sqrt(g)) ):
        if g%x==0:
            s+=2
    return s 
'''print ygs(28)'''

def tr(n):
    j=0
    for x in range (1,n+1):
        j=j+x
    return j
'''print tr(7)'''     

tr=0
for x in range (1,1000000):
    tr+=x
    n=ygs(tr)
    print x,n
    if n>=500:
        print tr
        break
 