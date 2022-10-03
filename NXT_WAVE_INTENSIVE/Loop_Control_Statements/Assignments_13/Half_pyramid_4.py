a = int(input())
b = int(input())
k=l=0
for i in range(0,b+1):
    k+=i
l=k+a-1
for j in range(1,b+1):
    for i in range(1,j+1):
        print(l,end=' ')
        l-=1
    print()
