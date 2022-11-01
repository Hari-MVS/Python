n=input()
d={}
count=0
for i in n:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
for i in d.values():
    if i>1:
        count+=1

print(count)
