def mi(base,power):
    d=0
    for y in str(base):
        d+=pow(int(y), power)
    return d
f=0
for d in range(2,10000000):
    if mi(d,5)==d:
        f+=d
print f

        
        
             