n=[int(i) for i in input().split(',')]
k=int(input())
new=[]
for i in n:
    for j in n:
        if i+j==k:
            if sorted((i,j)) not in new :
                new.append(sorted((i,j)))
for i in sorted(new):
    print(tuple(i))

# for i in range(len(re)):
#     if re[i] not in new:
#         new.append(re[i])
# print(new)
        
       
