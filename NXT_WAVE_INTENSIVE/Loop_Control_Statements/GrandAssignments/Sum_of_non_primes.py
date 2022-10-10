a = int(input())
sum=0
for i in range(a):
    count=0
    b = int(input())
    for j in range(2,b+1):
        if j==b:
            break
        if b%j==0:
            count+=1
    if count>=1:
        sum+=b
print(sum)
