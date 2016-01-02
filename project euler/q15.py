cache={}
def l(x,y):
    k=cache.get((x,y))
    if not k:
        if x==0 or y==0:
            k=1
        else:
            k=l(x-1,y)+l(x,y-1)
        cache[x,y]=k
    return k
print l(20,20)