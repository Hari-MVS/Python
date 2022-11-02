a,b=[int(i) for i in input().split()]
heights=[int(i) for i in input().split()]
for i in range(b):
    count=0
    tem=int(input())
    for j in heights:
        if j>=tem:
            count+=1
    print(count)
