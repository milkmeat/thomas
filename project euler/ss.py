def isprime(n):
    for x in range(2,n):       
        if n%x==0:
            return False
    return True
h=0
for J in range(1,10000):
    if isprime(J):
        h+=J
print h
    