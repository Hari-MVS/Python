n=int(input())
new=[]
for i in range(n):
    m=[int(i) for i in input().split()]
    if sum(m)==sum(set(m)):
        new.append(m)
print(new)
