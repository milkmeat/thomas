def d(n):
    zys=0
    for a in range(1,n):
        if n%a==0:
            zys+=a
            
    return zys
zzs=0
for a in range(1,10000):
    b=d(a)
    if a!=b and d(b)==a:
        zzs=zzs+(a+b)/2
print zzs
         
            