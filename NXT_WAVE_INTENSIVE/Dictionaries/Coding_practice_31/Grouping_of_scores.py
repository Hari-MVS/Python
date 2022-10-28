

re={}
for i in input().split(','):
    if i[0] in re:
        re[i[0]]=int(i[2:])+re[i[0]]
    else:
        re[i[0]]=int(i[2:])

print([(i,j) for i,j in sorted(re.items())])
