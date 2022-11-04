r,c=[int(i) for i in input().split()]
mat=[]
for i in range(r):
    temp=[]
    for j in input().split():
        temp.append(int(j))
    mat.append(temp)

pos_li=[]
for i in range(r):
    for j in range(c):
        summ=0
        if mat[i][j]==0 :
            pos_li.append((i,j))
            if j<c-1:
                if (i,j+1) not in pos_li:
                    summ+=mat[i][j+1]
            if j>0:
                if (i,j-1) not in pos_li:
                    summ+=mat[i][j-1]
            if i<r-1:
                if (i+1,j) not in pos_li:
                    summ+=mat[i+1][j]
            if i>0:
                if (i-1,j) not in pos_li:
                    summ+=mat[i-1][j]
            mat[i][j]=summ
 
values=[i[1] for i in pos_li]
keys=[i[0] for i in pos_li ]
for i in range(r):
    for j in range(c):
        if (i,j) not in pos_li:
            if i in keys:
                mat[i][j]=0
            elif j in values:
                mat[i][j]=0

for i in mat:
    for j in i:
        print(j,end=' ')
    print()



















