import copy
import math
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
    if prime<2:
        return False
    for x in range(2,int(math.sqrt(prime))+1):
        if prime%x==0:
            return False
    return True



for d1 in range(1,9+1):
    for d2 in range(d1,9+1):
        for d3 in range(d2,9+1):
            for d4 in range(d3,9+1):
                s=set()
                #['4','1','8','7']
                #print permutation([str(d1),str(d2),str(d3),str(d4)])
                for a in permutation([str(d1),str(d2),str(d3),str(d4)]):
                    if isprime(int(a)):
                        s.add(int(a))

                p=sorted(list(s))

                for a in range(len(p)):
                    for b in range(a+1, len(p)):
                        for c in range(b+1, len(p)):
                            if p[b]-p[a]==p[c]-p[b]:
                                print p[a],p[b],p[c]


