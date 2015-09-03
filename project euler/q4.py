def pal(p):
    s=str(p)
    for x in range(0,len(s)/2):
        if s[x]!=s[-1*(x+1)]:
            return False
    return True
    
max=0    
for x in range (100,1000):
    for y in range(100,1000):
        if pal(x*y):
            if x*y>max:
                max=x*y

print max            