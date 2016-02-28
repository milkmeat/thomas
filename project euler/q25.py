fib=[0]*5000
fib[0]=1
fib[1]=1
g=0
for x in range(2,len(fib)):
    g+=1
    fib[x]=fib[x-1]+fib[x-2]
    x=len(str(fib[x]))
    if x==1000:
        print g+2
        break

    
    