def pan(a,b,c):
    all = str(a)+str(b)+str(c)
    if "0" in all:
        return False
    if len(all)!=9:
        return False
    if len(set(all))!=9:
        return False  
    else:
        return True
p=0
f=set()
for x in range(1,9876):
    for y in range(x,9876):
        z=x*y
        if pan(x,y,z):
            f.add(z)
for d in f:
    p+=d
print p