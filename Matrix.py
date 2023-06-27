i=input().split()
m=int(i[0])
n=int(i[1])

l=[]
for i in range(1,m+1):
    j=list(map(int,input().split()))
    l.append(j)

j=0

lis=[]
while(j<n):
    sum1=0
    for i in range(0,m):
    
        sum1=sum1+l[i][j]
        
    j=j+1  
    lis.append(sum1)
m=max(lis)

l1=[]
j=0
for i in lis:
    if (i==m):
        l1.append(j+1)
    j=j+1
    
    
print(l1)