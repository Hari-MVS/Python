n=[int(i) for i in input().split()]
diff=[]
if len(set(n))==1 or sum(set(n))!=sum(n):
    diff.append(0)
else:
    for i in range(len(n)-1):
        for j in range(len(n)):
            if n[i]==n[j]:
                continue
            else:
                diff.append(abs(n[i]-n[j]))
print(min(diff))
