def isPrime(p):
    for x in range (2,p):
        if p%x==0:
            return False
    return True
'''
print isPrime(2)
print isPrime(3)
print isPrime(4)
print isPrime(5)
print isPrime(6)
print isPrime(7)
print isPrime(8)
'''
dijizhishu=0
ziranshu=1
while dijizhishu<10001:
    ziranshu+=1
    if isPrime(ziranshu):
        dijizhishu+=1
        print dijizhishu,ziranshu