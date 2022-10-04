a = int(input())
res =1
for i in range(a):
    for j in range(i+1):
        print(res,end=' ')
        res+=1
    print()
