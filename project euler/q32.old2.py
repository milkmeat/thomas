def pan(nd,er):
    p=nd*er
    n=set() 
    s=str(p)+str(er)+str(nd)
    for x in s:
        n.add(x)
    if str(0) in s:
        return False 
    if len(s)!=9:
        return False
    return  len(n)==len(s)         
h=0
c=set()
for y in range(1,9999):
    for x in range(1,9999):
        if pan(x,y):
            f=x*y
            c.add(f)
for f in c:
    h+=f
print h
       
        
    