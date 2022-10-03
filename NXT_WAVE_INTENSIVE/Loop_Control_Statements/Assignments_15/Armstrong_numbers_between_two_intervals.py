a = int(input())
b = int(input())
count=0
for i in range(a,b+1):
    s=str(i)
    tem=0
    for j in range(len(s)):
        tem+=int(s[j])**len(s)
    if tem==int(s):
        print(i,end=' ')
        count+=1
if count==0:
    print(-1)
