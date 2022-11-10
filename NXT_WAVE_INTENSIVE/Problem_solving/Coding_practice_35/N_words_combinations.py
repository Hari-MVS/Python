from itertools import combinations
m = sorted(input().split())
n=int(input())
re=list(sorted(set(combinations(m, n))))

for i in re:
    print(*i)
