list_a = [5, 20, 3, 7, 6, 8]
k = int(input())

list_a=sorted(list_a)
list_len = len(list_a)
res = list_a[list_len-n]
for i in range(n):
    res[i]=str(res[i])

print(" ".join(res))




# res = sorted(list_a)[::-1]
# new=[]
# if k==0:
#     print(list_a[0])
# else:
#     for i in range(k):
#         new.append(res[i])
# for i in sorted(new):
#     print(i,end=' ')
