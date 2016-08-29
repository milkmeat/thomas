def isprime(x):
    if x<=1:
        return False
    for y in range (2,x/2+1):
        if x%y==0:
            return False
    return True
#print isprime(1)
def left(c):
    o=str(c)
    for z in range(len(str(c))):
        x=o[z:]
        #print x
        if not isprime(int(x)):
            return False
    return True
def right(b):
    o=str(b)
    for z in range(1,len(str(b))+1):
        x=o[:z]
        #print x
        if not isprime(int(x)):
            return False
    return True

f=0
for m in range(11,1000000):
    if left(m) and right(m):
        print m
        f+=m
print f


