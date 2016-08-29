import copy

def pandigital(p):
    a=set()
    for x in str(p):
        a.add(x)
    if len(a)!=10:
        return False
    return True
def d(number,strnumber):
    return strnumber[number-1:number+2]
def p(primepandigital):
    prime=[2,3,5,7,11,13,17]
    
    if pandigital(primepandigital):
        for x in range(2,len(str(primepandigital))-1):
            divisible=d(x,str(primepandigital))
            if int(divisible)%prime[x-2]!=0:
                return False
        return True
    return False

#print p(1406357289)
'''    
h=0
b=1023456789
while b<9876543210:
    b+=1
    if b%1000000==0:
        print b
    if p(b):
        h+=b
print h
'''

def generate(digit):
    if len(digit)==1:
        yield digit[0]
    if len(digit)>0:
        for x in digit:
            other = copy.deepcopy(digit)
            other.remove(x)
            for rest in generate(other):
                yield x+rest


digit=['0','1','2','3','4','5','6','7','8','9']

h=0
for s in generate(digit):
    n=int(s)
    if p(n):
        h+=n
print h
