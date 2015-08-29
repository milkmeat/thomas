N=600851475143L

def isPrime(p):
    if p==1:
        return False
    for d in range (2,p):
        if p/d*d==p:
            return False
    return True
            

x=0L
while x<=N:
    x+=1
    if  N/x*x==N:
        if isPrime(x):
            print x
        