n=int(input())
mat=[]
for i in range(n):
    temp=[]
    for j in input().split():
        temp.append(int(j))
    mat.append(temp)
upp=0
low=0
for i in range(n):
    for j in range(n-i):
        upp+=mat[i][j]
    for j in range(i+1):
        low+=mat[i][n-j-1]
print(upp)
print(low)
