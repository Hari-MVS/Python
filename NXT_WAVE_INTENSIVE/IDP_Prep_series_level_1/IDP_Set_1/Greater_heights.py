a,b=input().split()
a=int(a)
b=int(b)
heights=[int(i) for i in input().split()]
for i in range(b):
    count=0
    tem=int(input())
    for j in heights:
        if j>=tem:
            count+=1
    print(count)
