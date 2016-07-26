def pan(nd,er):
    p=nd*er
    a=set()
    d=str(p)+str(nd)+str(er)    
    if '0' in d:
        return False 
    if len(d)==9:        
        for x in d:
            a.add(int(x))
    if len(a)!=len(d):       
        return False    
    return len(a)==9
g=0
b=set()
for x in range(1,9999):
    for y in range(1,9999):
        if pan(x,y):
            h=x*y
            b.add(h)
            print x,y,h
for x in b:
    g+=x
print g

            

    