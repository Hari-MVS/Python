l =input().split(" ")
lar=int(l[0])
for i in l:
    if int(i)>lar:
        lar=int(i)
print(lar)
