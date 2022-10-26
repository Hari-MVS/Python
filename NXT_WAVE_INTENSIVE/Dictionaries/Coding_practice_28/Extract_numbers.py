n=[i for i in input().split(',')]
new=[]
for i in n:
    if i.isdigit():
        new.append(i)
print([int(i) for i in new])
