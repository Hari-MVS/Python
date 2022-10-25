n=[int(i) for i in input().split(' ')]
new=[]
for i in n:
    if i not in new:
        new.append(i)
print(sorted(new))
