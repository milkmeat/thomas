d=[0]*(2000000+1)
d[0]=2
d[1]=2
for x in range (2,2000001):
    if d[x]==0:
        d[x]=1
        bei=x
        while bei+x<=2000000:
            bei+=x
            d[bei]=2
def isprime(p):
    return d[p]==1 
s=0
for x in range(2,2000000):
    if isprime(x):
        s=s+x
print s