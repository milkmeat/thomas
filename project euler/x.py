import math,time
def isOk(temp):
	if temp < 0: return False
	for i in range(2,int(math.sqrt(temp))+1):
		if temp%i==0 :
 			return False
	return True

begin = time.time()
maxValue=0
lastValue=1
for a in range(-1000,1001):
	for b in range(-1000, 1001):
		n = 0	
		resu = 0
		while True:
			temp = n*n + a*n + b
			if(isOk(temp)):
				resu+=1
				n+=1
			else :
				break
		if resu>maxValue:
			maxValue = resu
			lastValue = a*b
print lastValue
end = time.time()
print end-begin