n=[int(i) for i in input().split()]
mis=sum(n)-sum(set(n))
count=0
pos=[]
for i in n:
    if i==mis:
        pos.append(count)
    count+=1
n=sorted(n)
kid=0


if len(n)<=2 and len(set(n))<=1:
    kid=n[0]+1
else: 
    for i in range(1,len(n)+1):
        if i not in n:
            kid=i
            break
print(mis,kid)
