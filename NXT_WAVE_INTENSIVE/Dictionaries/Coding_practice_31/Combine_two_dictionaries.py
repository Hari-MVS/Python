re={}


for i in range(2):
    val=input().split()
    num=[int(i) for i in input().split()]
    for j in range(len(val)):
        re[val[j]]=num[j]

print([(i,j) for i,j in sorted(re.items())])
    
    




    
