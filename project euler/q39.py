def z(p):
    n=0
    for x in range(1,p):
        for y in range(x,p):
            for z in range(y,p):
                if x+y+z==p and x*x+y*y==z*z:
                    # print x,y,z
                    n+=1
    return n
bestSolution=0
bestP=0
for x in range(1,1001):
    g=z(x)
    print x
    if bestSolution<g:
        bestSolution=g
        bestP=x
print bestP
