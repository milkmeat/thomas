s=0
d=1
while s<1000:
    s=s+1
    d=d*2
s=str(d)
h=0
for ch in s:
    f=int(ch)
    h=h+f
print h