n=[int(i) for i in input().split(',')]
m=int(input())
for i in range(m):
    n=n[1:]+[n[0]]
print(n)
