m,n=input().split()
m=int(m)
n=int(n)
mat=[int(j) for i in range(m) for j in input().split()]
mat=sorted(mat)
res=[]
for i in range(m):
    temp=[]
    for j in range(n):
        temp.append(mat.pop())
    res.append(temp)
for i in res[::-1]:
    for j in i[::-1]:
        print(j,end=' ') 
    print()
