
f=open('p022_names.txt')
s=f.read( )
f.close()
d=0
d=s.split(',')
m=[c.strip('"') for c in d]
m.sort()
s=0
d=0
for x in m:
    s+=1
    for asc in x:
        z=ord(asc)-64
        z=z*s
        d+=z
print d
    