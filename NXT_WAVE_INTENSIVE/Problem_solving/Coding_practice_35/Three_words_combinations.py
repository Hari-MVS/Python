a=sorted(input().split())
le=len(a)
se=[]
for i in range(le):
    for j in range(le):
        for k in range(le):
            if j==k or i==k or i==j:
                continue
            elif (a[i],a[j],a[k]) not in se:
                # if sorted((a[i],a[j],a[k])) not in se:
                se.append(tuple(sorted((a[i],a[j],a[k]))))
[print(*i) for i in sorted(set(se))]
# print(sorted(set(se)))
