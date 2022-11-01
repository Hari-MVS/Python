a = [int(i) for i in input().split()] 
b = int(input())                       
for i in range(b):
    sum=0
    m = [int(i) for i in input().split()]   
    for j in a:
        if j>=m[0] and j<=m[-1]:
            sum+=j
    print(sum)
