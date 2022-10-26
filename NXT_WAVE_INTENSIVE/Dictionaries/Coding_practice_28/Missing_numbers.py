n=[int(i) for i in input().split()]
re=[]
for i in range(1,max(n)):
    if i not in n:
        re.append(i)
print(sorted(re))
        
