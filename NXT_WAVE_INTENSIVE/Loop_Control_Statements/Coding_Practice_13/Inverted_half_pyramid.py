a = int(input())
for i in range(a+1):
    res=1
    for j in range(a-i):
        print(res,end=' ')
        res+=1
    print()
