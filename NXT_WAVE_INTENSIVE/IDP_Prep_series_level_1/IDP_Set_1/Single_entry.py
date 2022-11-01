n=[int(i) for i in input().split()]
d={}
for i in n:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
[print(i,end=' ') for i,j in d.items() if j==1]
