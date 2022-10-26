n=[int(i) for i in input().split()]
res=set(n)
print("True" if len(res)==1 else sorted(list(res)))
