n=int(input())
mat=[]
for i in range(n):
    temp=[]
    for j in input().split():
        temp.append(int(j))
    mat.append(temp)
flag=True    
for i in mat:
    temp=[]
    for j in i:
        if j in range(1,n+1):
            temp.append(j)
        else:
            flag=False
            break
    if sum(set(temp))!=sum(temp):
        flag=False
        break
print("True" if flag else "False")
