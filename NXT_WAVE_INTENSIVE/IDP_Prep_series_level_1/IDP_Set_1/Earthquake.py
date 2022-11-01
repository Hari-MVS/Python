a,b=input().split()
a=int(a)
b=int(b)
re=1
for i in range(1,(a-b)+1):
    re*=32
print(re)
    
