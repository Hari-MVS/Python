n=input().lower()
uniq=set(n)
uniq.discard(' ')
for i in sorted(uniq):
    print('{}: {}'.format(i,n.count(i)))




# d={}
# for i in n:
#     if i==' ':
#         continue
#     else:
#         if i not in d:
#             d[i]=1
#         else:
#             d[i]+=1

# for i in sorted(d.keys()):
#     print(i+':',d[i])
