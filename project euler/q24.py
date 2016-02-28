import copy
def permutation(all):
    if len(all)==1:
        yield all[0] 
    for first in all:
        other = copy.copy(all)
        other.remove(first)
        for r in permutation(other):
            yield first + r
letter=['0','1','2','3','4','5','6','7','8','9']
g=0
for f in permutation(letter):
    g=g+1
    if g==1000000:
        print f
        break