m=[int(i) for i in input().split()]
summ=sum(m)
re=[]
for i in range(len(m)):
    a=m[i:]
    le=len(a)
    for j in range(len(a)):
        temp=[]
        for k in range(le):
            temp.append(a[k])
        le-=1
        if sum(temp)>=summ:
            summ=sum(temp)
            re=temp
print(*re)
