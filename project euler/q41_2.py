import math
# [False,False,True,True,False,...]

def countallnumber(max):
    prime=[True]*(max+1)
    prime[0]=False
    prime[1]=False
    for x in range(2,int(math.sqrt(max))+1):
        if prime[x]==False:
            continue
        mutiple=x+x
        while mutiple<=max:
            prime[mutiple]=False
            mutiple+=x
    return prime
print countallnumber(25)
'''
def pandigital(digits):
    n=len(str(digits))
    f=set()
    for ch in str(digits):
        if int(ch)<=0 or int(ch)>n:
            return False
        f.add(ch)
    if len(f)!=n:
        return False
    return True

upper=987654321
isprime=countAllPrimes(upper)
#if isprime[3]:
#    print 'ok'
#print isprime(1001)
# print primes


v=0
for x in range(upper,1,-1):
    print x
    if isprime[x]:
        if pandigital(x):
                print x
                break
'''

