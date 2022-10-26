num_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}

n=[int(i) for i in input().split()]

if num_set.issuperset(n):
    print('Superset')
elif num_set.issubset(n):
    print('Subset')
elif num_set.isdisjoint(n):
    print('Disjoint Set')
