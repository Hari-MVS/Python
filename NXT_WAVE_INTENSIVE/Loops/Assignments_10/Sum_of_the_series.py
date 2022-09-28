a=int(input())
b=int(input())
product =1
sum= 0
for i in range(b):
    if i%2==0:
        sum+=(a**(product))
        product+=2
    else:
        sum-=(a**(product))
        product+=2
print(sum)
