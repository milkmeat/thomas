import math

def isprime(n):
    if n<=0:
        return False
    for x in range(2,int(math.sqrt(n))+1):
        if n%x==0:
            return False
    return True
def primefactor(pf):
    allpf=[]
    for x in range(2,pf/2):
        if pf%x==0 and isprime(x):
            allpf.append(x)
    return allpf
max=100000000
x=0
all=[False]*max
for x in range(max):
    all[x] = len(primefactor(x))==4
    consecutive = True
    for y in range(4):
        if x-y>=0 and not all[x - y]:
            consecutive = False

    if consecutive:
        print x-y
        exit(0)



