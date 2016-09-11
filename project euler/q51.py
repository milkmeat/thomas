def listprime(lp):
    prime=[True]*lp
    prime[0]=False
    prime[1]=False
    for x in range(lp):
        if prime[x]:
            bei=x+x
            while bei<lp:
                prime[bei]=False
                bei+=x
    return prime

def replaceStar(s):
    result=[]
    if '*' in s:
        for n in range(0,9+1):
            news = s.replace('*', str(n))
            if news[0]!='0':
                result.append(news)
    else:
        result.append(s)
    return result

primes=listprime(10000000)

def countPrime(list):
    result=[]
    for s in list:
        if primes[int(s)]:
            result.append(s)
    return result

# print countPrime(replaceStar('56**3'))
# print countPrime(replaceStar('*3'))
def generate(g):
    if g==0:
        yield ''
        return
    for other in generate(g-1):
        for first in '1234567890*':
            yield first+other




for x in generate(6):
    if len(countPrime(replaceStar(x)))==8:
        print countPrime(replaceStar(x))
