a = int(input())
b = int(input())
c = 0
for i in range(1,b+1):
    if ((a%i==0) and (b%i==0)):
        if (i >=c):
            c = i
print(a//c*b)
    
