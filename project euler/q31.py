'''
def e(value,target):
    d=0
    f=0
    g=0
    for x in range(0,4):
        d+=1
    for y in range(0,5):
        f+=1
    for g in range(0,21):
        g+=1
    c=d*f*g
    return c
print e(1,1)
'''
# 0.1, 0.2, 0.5
# x,   y,   z,
# 0.1*x+0.2*y+0.5*z  =?  2
#1p, 2p, 5p, 10p, 20p, 50p, 1 (100p) and 2 (200p)
# a   b  c   d     e    f     g              h
count=0

def check(s):
    if s==200:
        global count, a,b,c,d,e,f,g,h
        count+=1
        #print a,b,c,d,e,f,g,h,count
    return s>=200

for a in range(0,200+1):
    suma=a*1
    if check(suma):
        break
    for b in range(0,100+1):
        sumb=suma+b*2
        if check(sumb):
            break
        for c in range(0,40+1):
            sumc=sumb+c*5
            if check(sumc):
                break
            for d in range(0,20+1):
                sumd=sumc+d*10
                if check(sumd):
                    break
                for e in range(0,10+1):
                    sume=sumd+e*20
                    if check(sume):
                        break
                    for f in range(0,4+1):
                        sumf=sume+f*50
                        if check(sumf):
                            break
                        for g in range(0,2+1):
                            sumg=sumf+g*100
                            if check(sumg):
                                break
                            for h in range(0,1+1):
                                sumh = sumg+h*200
                                check(sumh)

print count    