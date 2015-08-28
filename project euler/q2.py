l=[0]*100
l[0]=1
l[1]=2
for x in range (2,100):
    l[x]=l[x-1]+l[x-2]
#print l
f=0
for c in l:
    if c%2==0 and c<4000000:
        f=f+c
print f