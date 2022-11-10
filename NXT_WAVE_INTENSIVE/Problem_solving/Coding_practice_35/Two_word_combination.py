a=sorted(input().split())

se=[]
for i in range(len(a)):
    for j in range(len(a)):
        if i==j :
            continue
        elif (a[i],a[j]) not in se:
            if (a[j],a[i]) not in se:
                se.append((a[i],a[j]))
[print(*i) for i in se]
        
    
