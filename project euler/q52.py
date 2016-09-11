def permuted(n1,n2):
    for a in str(n1):
        if not a in str(n2):
            return False
    for b in str(n2):
        if  not b in str(n1):
            return False
    return True

def pl(list):
    for x in list:
        if not permuted(list[1],x):
            return False
    return True

for x in range(1,1000000):
    l=[x,2*x,3*x,4*x,5*x,6*x]
    if pl(l):
        print x
        break