def listprime(max):
    prime=[True]*max
    prime[0]=False
    prime[1]=False
    for x in range(max/2):
        if prime[x]:
            bei=x+x
            while bei<max:
                prime[bei]=False
                bei+=x
    return prime
def listprimenumber(lpn):
    listprimelpn=listprime(lpn)
    l=[]
    for x in range(len(listprimelpn)):
        if listprimelpn[x]:
            l.append(x)
    return l
b=listprimenumber(100)
print b
count=3

for x in range(len(b)-count):
    sum=0
    for y in range(count):
        sum+=b[x+y]
    if sum in b:
        print sum
    #if b[x+0]+b[x+1]+b[x+2] in b:
    #    print b[x],b[x+1],b[x+2]