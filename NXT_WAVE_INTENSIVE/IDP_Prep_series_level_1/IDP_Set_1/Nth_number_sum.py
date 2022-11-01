n,m=input().split()
n=int(n)
m=int(m)
val=[int(i) for i in input().split()]
sum=0
for i in range(1,m+1):
    if i%n==0:
        sum+=val[i-1]
print(sum)
