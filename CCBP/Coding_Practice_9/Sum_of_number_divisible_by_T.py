a=int(input())
b=int(input())
c=int(input())
sum=0
for i in range(b,c+1):
    if i%a==0:
        sum+=i
print(sum)
