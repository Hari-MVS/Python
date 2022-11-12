def sq(mt,x,y,side):
    count=0
    for i in range(x,x+side):
        for j in range(y,y+side):
            if mt[i][j]==1:
                count+=1
            else:
                return 0
    return count

m,n=map(int,input().split())
mark={'X':1,'O':0}
mt=[[mark[i] for i in input().split()] for j in range(m)]
areas =[]
for x in range(m):
    for y in range(n):
        for side in range(1,min(n-y+1,m-x+1)):
            areas.append(sq(mt,x,y,side))
print(max(areas))

























# r,c=list(map(int,input().split()))
# mat=[]
# for i in range(r):
#     temp=[]
#     for j in input().split():
#         temp.append(j)
#     mat.append(temp)
# di={i:0 for i in range(c)}
# count=0
# maxx=0
# for i in range(r):
#     summ=0
#     for j in range(c):
#         if mat[i][j]=='X':
#             di[j]+=1
#             summ+=di[j]
#             count+=1
#         else:
#             if summ%==0:
#                 if summ>maxx:
#                     maxx=summ
#             else:
#                 if summ//2 >maxx:
#                     maxx=summ//2
#                 if count>maxx:
#                     maxx=count
#             count=0
#             summ=0
#     else:
#             if summ%2==0:
#                 if summ>maxx:
#                     maxx=summ
#             else:
#                 if summ//2 >maxx:
#                     maxx=summ//2
#                 if count>maxx:
#                     maxx=count
#             count=0
#             summ=0
# print(maxx)
