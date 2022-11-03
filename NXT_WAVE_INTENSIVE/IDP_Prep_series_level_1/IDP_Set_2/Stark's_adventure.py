n=int(input())
loc=["West","North","East","South"]
for i in range(n):
    tem=1
    for i in input():
        if i =='R':
            tem+=1
            if loc[tem]=='South':
                print('YES')
                break
        elif i== 'L':
            tem-=1
            if loc[tem]=='South':
                print('YES')
                break
    else:
        print('NO')
        
