def cps(x):
    ss=1
    while x!=1:
        if x/2*2==x:
            x=x/2
        else:
            x=x*3+1
        ss+=1
    return ss
print cps(13)
s=0
c=0
for x in range (1,1000000):
    print x
    if s<cps(x):
        s=cps(x)
        c=x
print c