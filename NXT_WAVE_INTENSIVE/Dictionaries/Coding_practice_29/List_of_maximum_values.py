n=int(input())
new=[]

for i in range(n):
    m=[int(i) for i in input().split()]
    new.append(max(m))
print(new)
