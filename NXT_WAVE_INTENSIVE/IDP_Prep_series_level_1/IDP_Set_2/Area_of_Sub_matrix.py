import copy
a,b=[int(i) for i in input().split()]
mat=[]
for i in range(a):
    temp=[]
    for j in input().split():
        temp.append(int(j))
    mat.append(temp)
k=int(input())
product=1

if k==1 and a<=2:
    print(0)
elif k>=a or k>=b  :
    print(0)
else:
    
    for j in range(k):
        for i in range(len(mat)):
            if i==0 or i==len(mat)-1:
                mat.pop(i)
    new=[]
    le=len(mat)
    for i in range(b):
        temp=[]
        for j in range(le):
            temp.append(mat[j][i])
        new.append(temp)
        
    for j in range(k):
        for i in range(len(new)):
            if i==0 or i==len(new)-1:
                new.pop(i)
    for i in new:
        for j in i:
            product*=j
    print(product)
    
        



# if k > len(mat)//2 or k > len(mat[0])//2:
# 		 print(0)
# else:
#     res = 1
#     for i in range(k, len(mat)-k):
#     	for j in range(k, len(mat[i])-k):
#     		res *= mat[i][j]
#     print(res)     
        
