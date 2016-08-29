def wulishu(d):
    number=[]
    g=0
    while len(number)<=d:
        g+=1
        number.extend(str(g))
    return number[d]
b=1
for v in [1,10,100,1000,10000,100000,1000000]:
    x=int(wulishu(v-1))
    print x
    b*=x
print b
