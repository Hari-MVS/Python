a = [i[::-1] for i in input().split()]

len1 = 0
len2=0
flag =True
if len(a[0])>len(a[1]):
    len1 = len(a[0])
    len2=len(a[1])
else:
    len1=len(a[1])
    len2=len(a[0])

for j in range(len1):
    if j<len1 and j<len2:
        sum = int(a[0][j])+int(a[1][j])
        if len(str(sum))>1:
            flag = False
    else:
        break
print("Easy" if flag else "Hard")
