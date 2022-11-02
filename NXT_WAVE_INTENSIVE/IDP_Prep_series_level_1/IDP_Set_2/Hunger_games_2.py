n=int(input())
for i in range(n):
    temp=[]
    n,m,s=[int(i) for i in input().split()]
    for j in range(m):
        if s<=n:
            temp.append(s)
            s+=1
        else:
            s=1
            temp.append(s)
            s+=1
    print(temp[-1])
        

    
