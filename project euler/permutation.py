import math
import copy
def permutation(s):
    if len(s)==1:
        return s
    all=[]
    for x in s:
        other=copy.deepcopy(s)
        other.remove(x)
        for rest in permutation(other):
            all.append(x+rest)
    return all
def isprime(prime):
    for x in range(2,math.sqrt(prime)):
        if prime%2==0:
            return False
    return True
j=0
for a in permutation(['a','b','c','d']):
    i
    print a