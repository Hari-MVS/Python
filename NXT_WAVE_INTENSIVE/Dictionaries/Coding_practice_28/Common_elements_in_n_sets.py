n=int(input())
tem=[int(i) for i in input().split()]

for i in range(n-1):
    sec=[int(i) for i in input().split()]
    tem=set(tem).intersection(set(sec))
print(sorted(list(tem)))
