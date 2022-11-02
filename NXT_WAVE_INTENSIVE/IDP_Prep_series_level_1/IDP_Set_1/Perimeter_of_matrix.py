r,c=[int(i) for i in input().split()]
mat=[]
for i in range(r):
    temp=[]
    for j in input().split():
        temp.append(int(j))
    mat.append(temp)

summ=0      
for i in range(r):
    for j in range(c):
        if i==0 or i==r-1 or j==0 or j==c-1:
            summ+=mat[i][j]
print(summ)
    
