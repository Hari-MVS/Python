num_list = [(1, 2, 3, 4, 5, 6), (2, 4, 6, 8), (1, 3, 5, 7)]
# Write your code here
n=int(input())
new=[]
for i in num_list:
    temp=i
    if n in i:
        n_ind=i.index(n)
        temp= i[:n_ind]+i[n_ind+1:]
    new.append(temp)
print(new)
# for i in num_list:
#     tem=[]
#     for j in i:
#         if n==j:
#             continue
#         else:
#             tem.append(j)
#     new.append(tuple(tem))
# print(new)
