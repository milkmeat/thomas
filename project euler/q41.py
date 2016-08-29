import math

# [2,3,5,7,11]
primes=[2]

def countAllPrimes(max):
    for num in range(2,max+1):
        hasfactor=False
        sq=math.sqrt(num)
        for p in primes:
            if p>sq:
                break
            if num%p==0:
                hasfactor = True
                break
        if not hasfactor:
            print num
            primes.append(num)

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
countAllPrimes(upper)
#print isprime(1001)
# print primes

v=0
for x in primes[::-1]:
    print x
    if pandigital(x):
        break

