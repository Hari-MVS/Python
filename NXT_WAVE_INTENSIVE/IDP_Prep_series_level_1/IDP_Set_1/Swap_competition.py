n=int(input())
for i in range(n):
    m=input().split()
    if sorted(m[0])==sorted(m[1]):
        print('YES',end=' ')
    else:
        print('NO',end=' ')
