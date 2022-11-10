from itertools import combinations

m = sorted(input().split())
for i in range(1, len(m)+1):
  pos = list(sorted(set(combinations(m, i))))
  for j in pos:
    print(' '.join(j))
