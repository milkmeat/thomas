def sumpower(base,power):
    product=1
    for x in range(1,power+1):
        product*=base
    y=0
    for z in str(product):
        y+=int(z)
    return y
max=0
for x in range(1,100+1):
    for y in range(1,100+1):
        if max<sumpower(x, y):
            max=sumpower(x, y)
print max