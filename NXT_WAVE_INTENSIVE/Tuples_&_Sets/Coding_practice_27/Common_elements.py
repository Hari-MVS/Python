n=[int(i) for i in input().split(',')]
m=[int(i) for i in input().split(',')]
re=[]
for i in n:
    if i in m:
        re.append(i)
        

print(sorted(re))
