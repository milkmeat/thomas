def pan(x,y):
    m=''
    for b in range(1,y+1):
        v=x*b
        m+=str(v)
    if len(m)!=9 or len(set(m))!=9 or '0' in m :
        return False,int(m)
    return True, int(m)
max=0
for x in range(1,9999):
    for y in range(1,9):
        b, number = pan(x,y)
        if b:
            print x,y,number
            if max<number:
                max=number
print max










