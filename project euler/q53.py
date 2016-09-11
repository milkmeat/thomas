def fac(f):
    y=1
    for x in range(1,f+1):
        y*=x
    return y
def combination(r,n):
    return fac(n)/(fac(r)*fac(n-r))
v=0
for big in range(1,101):
    for small in range(1,big+1):
        if combination(small,big) > 1000000:
            v+=1
print v