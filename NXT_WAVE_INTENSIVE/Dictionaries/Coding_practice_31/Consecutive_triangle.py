a=[int(i) for i in input().split(',')]
print(a)

i=len(a)
re={j:a[j] for j in range(i)}
while i>0:
    tem=[]
    for j in range(i-1):
        re[j]=re[j]+re[j+1]
        tem.append(re[j])
    if tem:
        print(tem)
    i-=1
    
