fib=[0]*10000
fib[0]=1
fib[1]=1
for x in range(2,len(fib)):
    fib[x]=fib[x-1]+fib[x-2]
    print fib[x]