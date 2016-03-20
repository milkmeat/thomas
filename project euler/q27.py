def isprime(n):
    if n<=0:
        return False    
    for x in range(2,n):
        if n%x==0:
            return False
    return True
def maxn(a,b): 
    n=0
    while True:
        g=n*n + a*n + b
        n+=1
        if not isprime(g):
            break
    return n
g=0
for x in range(-999,999):
    for y in range(-999,999):
        if g<maxn(x,y):
            g=maxn(x,y)
            z=x
            h=y
print z*h