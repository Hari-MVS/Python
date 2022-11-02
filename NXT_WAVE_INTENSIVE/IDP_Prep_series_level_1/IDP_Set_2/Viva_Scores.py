n=int(input())
m=[int(i) for i in input().split()]
count=0
for i in range(len(m)):
    tem=m[i:]
    count=0
    for j in tem :
        if j<m[i]:
            count+=1
    print(count,end=' ')
            
            
    
