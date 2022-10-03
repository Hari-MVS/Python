a=int(input())
count=0
res=0
for i in range(1,a+1):
    count=0
    for j in range(2,11):
        if i%j==0:
            count+=1
    if count==0:
        res+=1
print(res)
