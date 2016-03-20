matrix=[]
size=1001 
for x in range(0,size):
    d=[0]*size
    matrix.append(d)

# 0=right, 1=down, 2=left, 3=up
direction=[[1,0],[0,1],[-1,0],[0,-1]]

x=size/2
y=size/2
matrix[y][x]=1
g=2
dir=0
movenum=1
tomove=0
while g <= size*size:
    tomove=(movenum+1)/2
    for move in range(0, tomove):
        x+=direction[dir][0]
        y+=direction[dir][1]
        #print y,x,g
        matrix[y][x]=g
        g+=1
        if g > size*size:
            break
    dir+=1
    dir%=4
    movenum+=1    
p=0
for x in range(0,size): 
    p=p+matrix[x][x]
g=0
for x in range(0,size):
    g+=matrix[size-x-1][x]
print p+g-1
    