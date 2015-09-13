

for x in xrange(232792500,232792599):
    allpass=True
    for r in range(1,21):
        if x%r!=0:
            allpass=False
    if allpass:
        print x
