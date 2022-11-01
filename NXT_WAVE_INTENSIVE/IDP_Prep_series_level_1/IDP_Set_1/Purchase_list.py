n=[int(i) for i in input().split()]
d={}
for i in n:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
count=''
count1=''
for i,j in d.items():
    if len(count)==1 and len(count1)==1:
        break
    if j==1 and len(count1)<1:
        count1=str(i)
    if j>=2 and len(count)<1:
        count=str(i)
print(count1 if count1 else 'None')
print(count if count else 'None')
        
        
