arr = [int(i) for i in input().split()]
n = len(arr)
dep = [int(i) for i in input().split()]

arr.sort()
dep.sort()
pt = 1
res = 1
i = 1
j = 0
 
while (i < n and j < n):
    if (arr[i] <= dep[j]):
        pt += 1
        i += 1
    elif (arr[i] > dep[j]):
        pt -= 1
        j += 1
    if (pt > res):
        res = pt
 
print(res)
