def Triangle(T):
    return T*(2*T-1)
def Pentagonal(P):
    return P*(3*P-1)/2
def Hexagonal(H):
    return H*(2*H-1)

mini=100000

t=set()
p=set()
h=set()

for x in range(1,mini):
    t.add(Triangle(x))
    p.add(Pentagonal(x))
    h.add(Hexagonal(x))

print p.intersection(t).intersection(h)
