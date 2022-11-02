n=int(input())
for i in range(n):
    d={}
    count=0
    for j in range(int(input())):
        a=''.join(input().split())
        if a.lower() not in d:
            d[a.lower()]=1
        else:
            d[a.lower()]+=1
    for j in d.values():
        if j>=2:
            print('Yes')
            break
        else:
            print('No')
            break
        
        
