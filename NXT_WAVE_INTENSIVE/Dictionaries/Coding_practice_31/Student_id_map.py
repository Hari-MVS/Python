a=input().split(',')
b=input().split(',')

re={}
length=len(a)
for i in range(length):
    re[a[i]]=b[i]

for i,j in sorted(re.items()):
    print(i,j)


# re={a[i]:b[i] for i in range(len(a))}

# [print(i,j) for i,j in sorted(re.items())]
