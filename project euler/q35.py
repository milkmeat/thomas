def isprime(x):
    for y in range (2,x/2+1):
        if x%y==0:
            return False 
    return True 
def iscircular(z):
    s=str(z)
    for i in range(len(s)):
        a=s[1:]+s[0] 
        if not isprime(int(a)):
            return False 
        s=str(a)
    return True 
v=0
for x in range(2,1000000):
    if iscircular(x):
        print x
        v+=1
print v
    