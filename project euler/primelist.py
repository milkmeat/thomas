max=1000
prime=[True]*max
prime[0]=False
prime[1]=False
for x in range(max):
    if prime[x]:
        bei=x+x
        while bei<max:
            prime[bei]=False
            bei+=x
print prime[0]
