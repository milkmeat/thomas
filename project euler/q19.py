def isLeapYear(y):
    return y%4==0 and (y%400==0 or y%100!=0)
def dayInMonth(y,m):
    if m  in(1,3,5,7,8,10,12):
        return 31
    if m in(4,6,9,11):
        return 30
    if m==2:
        if isLeapYear (y):
            return  29
        else:
            return 28

def lastMonth(y,m):
    if m>1:
        return y, m-1
    if m==1:
        return y-1, 12
            
# Sunday =0
last1=6
count=0
for year in range(1901,2001):
    for month in range(1,13):
        ly, lm = lastMonth(year,month)
        d=dayInMonth(ly, lm)
        last1 = d%7 + last1
        last1 = last1%7
        if last1==0:
            count+=1
        print year, month, last1
print count
        
    