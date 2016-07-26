def c(m,z):
    z10=z/10
    z1=z%10
    m10=m/10
    m1=m%10
    if m1==0:
        return False 
    if z1==m10:
        if float(z)/float(m)==float(z10)/float(m1):
            return True
    return False
for x in range(10,100):
    for y in range(10,100):
        if c(x,y):
            print x,y