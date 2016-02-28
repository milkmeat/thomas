def a(n):
    zy=0
    for x in range(1,n):
        if n%x==0:
            zy+=x
    return zy>n

    
abundant=[]
for d in range(1,28124):
    if a(d):
        abundant.append(d)


total=0
for f in range(1,28124):
    print f
    total+=f
    for a in range(1,f):
        b=f-a
        if a in abundant and b in abundant:
            total-=f            
            break
print total