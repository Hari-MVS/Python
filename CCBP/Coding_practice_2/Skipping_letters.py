a = input()
b = int(input())
res = ''
for i in range(len(a)):
    if  i== b:
        continue
    else:
        res+=a[i]
print(res)
