def cf(fm):
    history=[]
    fz=1
    while fz not in history:
        history.append(fz)        
        fz*=10
        shang=fz/fm
        fz=fz%fm
    return len(history)-history.index(fz)
d=0
for x in range(2,1001):
    p=cf(x)
    if d<p:
        z=x
        d=p
print z