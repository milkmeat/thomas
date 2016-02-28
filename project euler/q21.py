def d(n):
    f=0
    for x in range(1,n):
        if n%x==0:
            f=f+x
    return f
c=0
for a in range(1,10000):
    b=d(a)
    if a!=b and d(b)==a:
        c=c+a+b
print c/2 
    