n=int(input())
n_list=[]
zero_index=[]
fir_index=[]
for i in range(n):
    val_lis=input().split()
    fir_val=int(val_lis[0])
    zero_index.append(fir_val)
    sec_val=int(val_lis[1])
    fir_index.append(sec_val)
zero_min_max_tup=(max(zero_index),min(zero_index))
fir_min_max_tup=(max(fir_index),min(fir_index))
print(zero_min_max_tup)
print(fir_min_max_tup)



# m=[tuple([int(i) for i in input().split()]) for i in range(n) ]
# mod=[]
# for i in range(2):
#     tem=[]
#     for j in range(len(m)):
#         tem.append(m[j][i])
#     mod.append(tuple((max(tem),min(tem))))
# [print(i) for i in mod]
    
