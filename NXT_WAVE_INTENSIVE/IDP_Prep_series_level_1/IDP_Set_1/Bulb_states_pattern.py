n=int(input())
temp=[]
for i in range(1,n+1):
    if i==1 or i%2!=0:
        temp.append(1)
    else:
        temp.append(0)
print(*temp)
for i in range(len(temp)-1):
    for j in range(len(temp)):
        if temp[j]==1:
            temp[j]=0
        else:
            temp[j]=1
    print(*temp)
