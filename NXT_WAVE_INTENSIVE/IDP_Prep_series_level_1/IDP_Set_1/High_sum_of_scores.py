n=int(input())
mat=[int(i) for i in input().split(',')]
summ=sum(mat)
for i in range(n-1):
    temp=[]
    for j in input().split(','):
        temp.append(int(j))
    if summ<sum(temp):
        summ=sum(temp)
        mat=temp

print(*mat)
    
