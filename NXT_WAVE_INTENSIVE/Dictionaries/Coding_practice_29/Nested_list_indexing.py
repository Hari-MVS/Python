num_list = [(2, 4, 6, 8), (5, 15, 25, 35), (7, 14, 21)]
n=int(input())
for i in num_list:
    temp= n in i
    if temp:
        ind=num_list.index(i)
        n_index=i.index(n)
        print(str(ind)+' '+str(n_index))
        break



# for i in range(len(num_list)):
#     for j in range(len(num_list[i])):
#         if n==num_list[i][j]:
#             print(i,j)
#             break
