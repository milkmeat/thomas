import math
def isprime(n):
    if n<=0:
        return False
    for x in range(2,n):
        if n%x==0:
            return False
    return True
def IScompostiveodd(co):
    if isprime(co)==False:
        if co%2==1:
            return True
    return False
def issqrt(s):
    f=math.sqrt(s)
    if f==int(f):
        return True
    return False
for x in range(10000):
    if IScompostiveodd(x)==True:
        isgood=False
        for p in range(2,x):
            if isprime(p):
                if issqrt((x-p)/2):
                    isgood=True
        if isgood==False:
            print x
            exit(0)


