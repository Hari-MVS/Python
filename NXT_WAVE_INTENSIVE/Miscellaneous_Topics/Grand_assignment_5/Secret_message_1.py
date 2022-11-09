alpha=[chr(i) for i in range(97,123)]
n=input().lower()
res=''
for i in n:
    if i==' ':
        res+=' '
    elif i in alpha:
        tem=alpha.index(i)
        res+=alpha[::-1][tem]
print(res)
