'''
def Pentagon(s):
    for x in range(1,s+1):
        if x*(3*x-1)/2==s:
            return True
    return False
a=10000
for j in range(1,10000):
    for k in range(1,10000):
        if Pentagon(j):
            if Pentagon(k):
                if Pentagon(j-k):
                    if Pentagon(j+k):
                        if a>abs(k-j):
                            a=abs(k-j)
print a
'''

def Pantagon(s):
    return s*(3*s-1)/2
mini=3000
minidiff=100000000000000000000000000
p=[]
for x in range(mini):
    print x
    p.append(Pantagon(x))
for j in range(1,mini):
    for k in range(j+1,mini):
        sum=p[j]+p[k]
        diff=p[k]-p[j]
        if sum in p and diff in p:
            if minidiff>diff:
                minidiff=diff
print minidiff
    