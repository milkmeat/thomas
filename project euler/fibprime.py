def d(n):
    for x in range(2,n):        
        if n%x==0:
            return False
    return True
for x in range(1,10):
    print x, d(x)
'''
fib=[0]*10000
fib[0]=1
fib[1]=1
for x in range(2,len(fib)):
    fib[x]=fib[x-1]+fib[x-2]
    if d(fib[x]):
       print fib[x]'''