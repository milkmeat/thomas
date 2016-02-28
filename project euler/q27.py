def d(n):
    if n<=0:
        return False
    for x in range(2,n):        
        if n%x==0:
            return False
    return True
def maxn(a,b):
    n=-0
    while True:
        n+=1
        if not d(n*n + a*n + b):
            break
    return n
g=0
for a in range(-999,999):
    for b in range(-999,999):
        if g<maxn(a,b):
            h=a
            f=b
            g=maxn(a,b)
print h*f