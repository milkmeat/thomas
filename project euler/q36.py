base = [str(x) for x in range(10)] + [ chr(x) for x in range(ord('A'),ord('A')+6)]
def bin2dec(string_num):
    return str(int(string_num, 2))
def dec2bin(string_num):
    num = int(string_num)
    mid = []
    while True:
        if num == 0: break
        num,rem = divmod(num, 2)
        mid.append(base[rem])
    return ''.join([str(x) for x in mid[::-1]])
def ispalindromic(x):
    b=str(x)
    for i in range (len(b)):
        if b[i]!=b[-(i+1)]:
            return False
    return True
v=0
for x in range(1,1000000):
    if ispalindromic(dec2bin(x)) and ispalindromic(x):
        v+=x
print v

