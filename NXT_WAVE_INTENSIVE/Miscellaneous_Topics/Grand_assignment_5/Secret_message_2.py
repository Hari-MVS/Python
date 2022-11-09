alpha=[chr(i) for i in range(97,123)]
n=input().lower()
res=str(alpha.index(n[0])+1)
for i in range(1,len(n)):
    if n[i]==' ':
        res+=' '
    else:
        if n[i-1] ==' ':
            res+=str(alpha.index(n[i])+1)
        elif n[i] in alpha:
            res+='-'+str(alpha.index(n[i])+1)
print(res)
