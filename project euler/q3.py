N=600851475143L
primes=[2]

def isPrime(p):
    if p==1:
        return False
    for d in primes:
        if d<p and p%d==0:
            return False
    return True
    
x=1
while x<N:
    x+=1
    if isPrime(x):
        primes.append(x)
        if  N%x==0L:
            print x
            N=N/x
            x=1
    
    
      