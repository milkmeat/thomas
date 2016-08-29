def selfpower(s):
    product=1
    for all in range(s):
        product*=s
    return product
sum=0
for x in range(1,11):
    sum+=selfpower(x)
print sum